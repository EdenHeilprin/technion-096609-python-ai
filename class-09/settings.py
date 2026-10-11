# oTree reads this list to populate the Create session menu.
SESSION_CONFIGS = [
    dict(
        name='seven_choices',
        display_name='Sure or gamble',
        num_demo_participants=2,
        app_sequence=['choice_task'],
        is_test=True,
    ),
]

# Points in this exercise are hypothetical and never paid.
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0, participation_fee=0)
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = None
DEMO_PAGE_INTRO_HTML = ''

# A fixed public key is sufficient only for this local teaching project.
SECRET_KEY = 'class-09-local-practice-not-for-public-hosting'
INSTALLED_APPS = ['otree']
