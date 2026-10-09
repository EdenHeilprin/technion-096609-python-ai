"""A one-decision starting point for the sure-or-gamble study."""

from otree.api import *


class C(BaseConstants):
    # This app has one decision, with participants working independently.
    NAME_IN_URL = "choice_task"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    STUDY_VERSION = "minimal-v1"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Save the offer and version with the response, not only in the page's text.
    study_version = models.StringField(initial=C.STUDY_VERSION)
    sure_points = models.IntegerField(initial=4)
    gamble_high = models.IntegerField(initial=10)
    gamble_probability = models.FloatField(initial=0.5)

    # Neither option is preselected. The server accepts only these two values.
    choice = models.StringField(choices=["sure", "gamble"])


class Choice(Page):
    # Connect the HTML form to the response saved in this Player record.
    form_model = "player"
    form_fields = ["choice"]

    # Restore an unfinished selection after a refresh in the same browser.
    preserve_unsubmitted_inputs = True


class ThankYou(Page):
    # This page confirms that the preceding response has already been saved.
    pass


# The participant sees the choice first and the confirmation second.
page_sequence = [Choice, ThankYou]


def custom_export(players):
    # Keep the same export structure as the later six-round version.
    yield [
        "session_code", "participant_code", "study_version", "round_number",
        "sure_points", "gamble_high", "gamble_probability", "choice", "confidence",
    ]
    for player in players:
        # An unfinished response remains blank rather than becoming a choice.
        choice = player.field_maybe_none("choice")
        yield [
            player.session.code, player.participant.code, player.study_version,
            player.round_number, player.sure_points, player.gamble_high,
            player.gamble_probability, choice if choice is not None else "", "",
        ]
