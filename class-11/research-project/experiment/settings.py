"""Local teaching settings with explicit safeguards for a hosted deployment."""

from os import environ


SESSION_CONFIGS = [
    dict(
        name="sure_or_gamble",
        display_name="Sure or gamble — six decisions",
        num_demo_participants=1,
        app_sequence=["choice_task"],
    ),
]

# The task uses hypothetical points and never calculates payments.
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0, participation_fee=0, doc="")
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "ILS"
USE_POINTS = True
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = environ.get("OTREE_ADMIN_PASSWORD")

# This public fallback is for local development only, never a production secret.
DEVELOPMENT_SECRET_KEY = "local-only-sure-or-gamble-development-key"
SECRET_KEY = environ.get("OTREE_SECRET_KEY", DEVELOPMENT_SECRET_KEY)
DEMO_PAGE_INTRO_HTML = "A classroom pilot using hypothetical points; no payments."

# Fail closed on a hosted dyno or when production mode is explicitly requested.
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
