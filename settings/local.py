# This Normally Should not be Committed to the Repository, but is in this case as an example.
from pinax_settings.settings.pinax import MIDDLEWARE_CLASSES
from pinax_settings.settings.project import INSTALLED_APPS

MIDDLEWARE_CLASSES += ["debug_toolbar.middleware.DebugToolbarMiddleware",]

INSTALLED_APPS += ["debug_toolbar",]

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}