import random
import time
from otree.api import (
    BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page, models, widgets,
)

doc = 'Seven hypothetical choices between 10 sure points and a 50/50 gamble.'


# oTree reads these constants to identify the app and create its seven rounds.
class C(BaseConstants):
    NAME_IN_URL = 'choice_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 7
    PRIZES = [2, 8, 14, 20, 26, 32, 38]
    SURE_POINTS = 10


# A Subsession contains all participants in one round of this app.
class Subsession(BaseSubsession):
    pass


# oTree requires a Group structure even though participants decide independently.
class Group(BaseGroup):
    pass


# oTree stores one Player record per participant per round.
class Player(BasePlayer):
    # These details are collected and saved only in the first round.
    consent = models.BooleanField(
        label='I am 18 or older and voluntarily consent to participate.',
        widget=widgets.CheckboxInput,
        blank=True,
    )
    subject_id = models.StringField(label='Prolific ID or made-up classroom ID')
    age = models.IntegerField(label='Age (optional)', min=18, max=120, blank=True)
    gender = models.StringField(
        label='Gender',
        choices=['Woman', 'Man', 'Non-binary', 'Other', 'Prefer not to say'],
        widget=widgets.RadioSelect,
        blank=True,
    )
    condition = models.StringField()
    is_test = models.BooleanField()
    # Save the finishing time once so the first completed duplicate can be retained.
    completed_at = models.FloatField(blank=True)
    # These fields describe the displayed choice in each of the seven rounds.
    prize = models.IntegerField()
    choice = models.StringField(
        choices=[['sure', 'Option A'], ['gamble', 'Option B']],
        widget=widgets.RadioSelect,
        label='Choose one option',
    )


def prize_for_round(condition, round_number):
    # Make a fresh list so reversing it cannot change the original prizes.
    prizes = list(C.PRIZES)
    if condition == 'descending':
        prizes.reverse()
    # Round numbers start at 1, but Python list positions start at 0.
    return prizes[round_number - 1]


def creating_session(subsession):
    # oTree calls this function once for each round when a session is created.
    players = subsession.get_players()
    if subsession.round_number == 1:
        # Alternating labels give equal groups, with one extra person if needed.
        conditions = []
        for index in range(len(players)):
            if index % 2 == 0:
                conditions.append('ascending')
            else:
                conditions.append('descending')
        # Shuffle the labels so participant position does not determine order.
        random.shuffle(conditions)
        for index in range(len(players)):
            players[index].condition = conditions[index]
            players[index].is_test = subsession.session.config['is_test']

    for player in players:
        # Read the original assignment, so the condition never changes mid-task.
        first_round = player.in_round(1)
        player.prize = prize_for_round(first_round.condition, player.round_number)


class Consent(Page):
    # Hide developer details from participant pages, even on the devserver.
    is_debug = False
    # form_model and form_fields tell oTree where to save submitted answers.
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def is_displayed(player):
        # oTree uses this method to decide whether to show the page.
        return player.round_number == 1

    @staticmethod
    def error_message(player, values):
        # Consent is required to continue; participants can instead close the tab.
        if not values['consent']:
            return 'To participate, confirm that you are 18 or older and consent. You may close this tab to stop.'


class Details(Page):
    # Hide developer details from participant pages, even on the devserver.
    is_debug = False
    form_model = 'player'
    form_fields = ['subject_id', 'age', 'gender']

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

    @staticmethod
    def error_message(player, values):
        # Reject an ID containing only spaces, which cannot identify a run.
        if not values['subject_id'].strip():
            return 'Please enter your Prolific ID or a made-up classroom ID.'

    @staticmethod
    def before_next_page(player, timeout_happened):
        # Remove accidental spaces before saving the ID for duplicate checks.
        player.subject_id = player.subject_id.strip()


class Decision(Page):
    # Hide developer details from participant pages, even on the devserver.
    is_debug = False
    form_model = 'player'
    form_fields = ['choice']

    @staticmethod
    def vars_for_template(player):
        # This dictionary supplies named values to the HTML template.
        return dict(sure_points=C.SURE_POINTS, total_rounds=C.NUM_ROUNDS)

    @staticmethod
    def before_next_page(player, timeout_happened):
        # The seventh choice has been saved before oTree shows the thank-you page.
        if player.round_number == C.NUM_ROUNDS:
            player.in_round(1).completed_at = time.time()


class ThankYou(Page):
    # Hide developer details from participant pages, even on the devserver.
    is_debug = False

    @staticmethod
    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


# oTree follows this sequence in every round, skipping pages as specified above.
page_sequence = [Consent, Details, Decision, ThankYou]
