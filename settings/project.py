from pinax_settings.settings.paths import PROJECT_ROOT
from pinax_settings.settings.pinax import INSTALLED_APPS, STATICFILES_DIRS, TEMPLATE_DIRS
import posixpath
import os.path

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "dev.db",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

SITE_ID = 1

USE_I18N = True
USE_L10N = True

TIME_ZONE = "US/Eastern"
LANGUAGE_CODE = 'en-us'

SECRET_KEY = "7n#vuyn9q(5$sp#irdz@mlkt9vz%)y551)ulo6996$vqgc-9pf"

STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, "static"),] + STATICFILES_DIRS

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")
MEDIA_URL = "/site_media/media/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")
STATIC_URL = "/site_media/static/"

ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, "templates"),] + TEMPLATE_DIRS

INSTALLED_APPS += [
    "about",
    "profiles",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]