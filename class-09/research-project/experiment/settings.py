"""Local settings for the one-choice checkpoint."""

from os import environ


SESSION_CONFIGS = [
    dict(
        name="sure_or_gamble",
        display_name="Sure or gamble — one decision",
        num_demo_participants=1,
        app_sequence=["choice_task"],
    ),
]

# This teaching task uses hypothetical points, with no payments.
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0, participation_fee=0, doc="")
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "ILS"
USE_POINTS = True
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

# This public fallback is safe only for development on your own computer.
DEVELOPMENT_SECRET_KEY = "local-only-sure-or-gamble-development-key"
SECRET_KEY = environ.get("OTREE_SECRET_KEY", DEVELOPMENT_SECRET_KEY)
DEMO_PAGE_INTRO_HTML = "One hypothetical decision; no payments."

# A hosted server must use private credentials and protect its administration pages.
if environ.get("DYNO") or environ.get("OTREE_PRODUCTION"):
    if not environ.get("OTREE_SECRET_KEY") or len(SECRET_KEY) < 32 or SECRET_KEY == DEVELOPMENT_SECRET_KEY:
        raise RuntimeError("Set OTREE_SECRET_KEY to a private random value of at least 32 characters.")
    if not ADMIN_PASSWORD or len(ADMIN_PASSWORD) < 12:
        raise RuntimeError("Set a private OTREE_ADMIN_PASSWORD of at least 12 characters.")
    if environ.get("OTREE_AUTH_LEVEL") != "STUDY":
        raise RuntimeError("Set OTREE_AUTH_LEVEL=STUDY to protect the hosted administration pages.")
    if environ.get("OTREE_PRODUCTION") != "1":
        raise RuntimeError("Set OTREE_PRODUCTION=1 on the hosted server.")
    if environ.get("DYNO") and not environ.get("DATABASE_URL"):
        raise RuntimeError("Attach the production database before launching a hosted study.")
