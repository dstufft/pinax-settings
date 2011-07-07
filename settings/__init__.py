# Base Settings
from pinax_settings.settings.base import *

# Django Settings; Things that deal directly with Django and it's apps
from pinax_settings.settings.django import *

# Pinax Settings (anything Pinax Overrides or Sets by Default)
from pinax_settings.settings.pinax import *

# Project Settings (Anything Specific to this Project)
from pinax_settings.settings.project import *

# settings/local.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from pinax_settings.settings.local import *
except ImportError:
    pass