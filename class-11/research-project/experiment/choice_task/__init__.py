"""Six hypothetical sure-or-gamble decisions for the classroom pilot."""

from otree.api import *


class C(BaseConstants):
    # oTree uses this name in participant URLs and groups no participants together.
    NAME_IN_URL = "choice_task"
    PLAYERS_PER_GROUP = None

    # Every participant sees these six guaranteed offers in this order.
    SURE_OFFERS = [2, 3, 4, 6, 7, 8]
    NUM_ROUNDS = len(SURE_OFFERS)
    GAMBLE_HIGH = 10
    GAMBLE_PROBABILITY = 0.5
    STUDY_VERSION = "full-v1"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Save the design alongside each response so the export describes this session.
    study_version = models.StringField()
    sure_points = models.IntegerField()
    gamble_high = models.IntegerField()
    gamble_probability = models.FloatField()

    # Only these two values are accepted by the server; neither is preselected.
    choice = models.StringField(choices=["sure", "gamble"])

    # The server requires one of the seven integers, even if JavaScript is disabled.
    confidence = models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelect
    )


def creating_session(subsession):
    # Round numbers start at 1; list positions start at 0.
    offer = C.SURE_OFFERS[subsession.round_number - 1]
    for player in subsession.get_players():
        player.study_version = C.STUDY_VERSION
        player.sure_points = offer
        player.gamble_high = C.GAMBLE_HIGH
        player.gamble_probability = C.GAMBLE_PROBABILITY


class Welcome(Page):
    @staticmethod
    def is_displayed(player):
        # Show the introduction once, before the first decision.
        return player.round_number == 1


class Choice(Page):
    # oTree saves valid submitted answers to this round's Player record.
    form_model = "player"
    form_fields = ["choice", "confidence"]

    # Restore unfinished selections after a refresh in the same browser.
    # They are only saved to the server after the participant submits the page.
    preserve_unsubmitted_inputs = True


class ThankYou(Page):
    @staticmethod
    def is_displayed(player):
        # After the final saved choice, show a receipt instead of another task.
        return player.round_number == C.NUM_ROUNDS


# oTree repeats this sequence for each round, skipping pages when specified above.
page_sequence = [Welcome, Choice, ThankYou]


def custom_export(players):
    # A row represents one participant in one round, not one whole participant.
    yield [
        "session_code", "participant_code", "study_version", "round_number",
        "sure_points", "gamble_high", "gamble_probability", "choice", "confidence",
    ]
    for player in players:
        # Unfinished rounds have no submitted answers; preserve those missing values.
        choice = player.field_maybe_none("choice")
        confidence = player.field_maybe_none("confidence")
        yield [
            player.session.code, player.participant.code, player.study_version,
            player.round_number, player.sure_points, player.gamble_high,
            player.gamble_probability,
            choice if choice is not None else "",
            confidence if confidence is not None else "",
        ]
