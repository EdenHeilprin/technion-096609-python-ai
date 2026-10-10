from otree.api import *  # Load the building blocks supplied by oTree.


class C(BaseConstants):
    # Set the web address name and let each participant work independently.
    NAME_IN_URL = "sure_or_gamble"
    PLAYERS_PER_GROUP = None

    # Use one guaranteed offer per round, in this order.
    SURE_OFFERS = [2, 3, 4, 6, 7, 8]
    NUM_ROUNDS = len(SURE_OFFERS)


# oTree requires these two containers; this experiment needs no extra fields in them.
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Save this round's offer and the participant's answer.
    offer = models.IntegerField()
    choice = models.StringField(choices=["Sure", "Gamble"], widget=widgets.RadioSelect)


def creating_session(subsession):
    # oTree numbers rounds from 1; Python numbers list positions from 0.
    offer = C.SURE_OFFERS[subsession.round_number - 1]
    for player in subsession.get_players():
        player.offer = offer


class Choice(Page):
    # Connect the answer on the HTML page to the saved choice field.
    form_model = "player"
    form_fields = ["choice"]


class ThankYou(Page):
    @staticmethod
    def is_displayed(player):
        # Show the final page only after the sixth choice.
        return player.round_number == C.NUM_ROUNDS


# oTree repeats this page sequence for each round.
page_sequence = [Choice, ThankYou]


def custom_export(players):
    # oTree uses yield to add each row to the downloadable CSV.
    yield ["session", "participant", "offer", "choice"]
    for player in players:
        # field_maybe_none leaves unfinished answers empty in the export.
        yield [player.session.code, player.participant.code,
               player.offer, player.field_maybe_none("choice")]
