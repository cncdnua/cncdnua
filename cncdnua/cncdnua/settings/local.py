from .base import *  # noqa
from .twitter import *  # noqa
from .github import *  # noqa


# extending settings for debug toolbar

DEBUG = True

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
