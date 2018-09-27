from .common import Common


class Production(Common):
    DEBUG = False

    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS.append('gunicorn')

    ALLOWED_HOSTS = ["*"]
