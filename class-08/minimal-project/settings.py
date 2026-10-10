"""oTree configuration for local rehearsal of the Class 8 demonstration."""
from os import environ

SESSION_CONFIGS = [dict(name="sure_or_gamble", display_name="Sure or Gamble",
                       num_demo_participants=1, app_sequence=["choice_task"])]
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0, participation_fee=0, doc="")
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
LANGUAGE_CODE = "en"
REAL_WORLD_CURRENCY_CODE = "ILS"
USE_POINTS = True
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = None
SECRET_KEY = "class-8-local-rehearsal-only"

# Hosting is a separate step; do not expose this local review configuration online.
if environ.get("DYNO") or environ.get("OTREE_PRODUCTION") or environ.get("DATABASE_URL"):
    raise RuntimeError("This configuration is for local rehearsal. Configure secure hosting separately.")
