# Python imports
from os.path import join

# project imports
from .common import *
from .jazzmin import *
# uncomment the following line to include i18n
# from .i18n import *


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# adjust the minimal login
LOGIN_URL = 'admin'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'admin'


# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR.parent / "run" / "dev.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}


CUSTOM_APPS = [
    'import_export',
    'admin_section.apps.AdminSectionConfig',
    'course.apps.CourseConfig',
    'team.apps.TeamConfig',
    'study_material.apps.StudyMaterialConfig',
    'blog.apps.BlogConfig',
    'news.apps.NewsConfig',
]
# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS + CUSTOM_APPS
