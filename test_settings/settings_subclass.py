from .settings import *

INSTALLED_APPS += [
    'test_boxme_user_subclass',
]
AUTH_USER_MODEL = 'test_boxme_user_subclass.MyCustomBoxmeUser'
