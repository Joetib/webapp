# test_settings.py
import pytest
from django.conf import settings

def test_debug_mode():
    assert settings.DEBUG is True, "Check if DEBUG mode is set to True for testing"

def test_secret_key():
    assert settings.SECRET_KEY == 'django-insecure-m#*+c#=%80gsv1ddca91&2u!za@5cfrpx@b-_e&%^1t%c#2zh_', "Check if SECRET_KEY matches the expected value"

def test_allowed_hosts():
    assert settings.ALLOWED_HOSTS == ['*'], "Check if ALLOWED_HOSTS includes '*'"

def test_installed_apps():
    assert 'django.contrib.admin' in settings.INSTALLED_APPS, "Check if 'django.contrib.admin' is in INSTALLED_APPS"
    assert 'pages' in settings.INSTALLED_APPS, "Check if 'pages' app is in INSTALLED_APPS"

def test_middleware():
    assert 'django.middleware.security.SecurityMiddleware' in settings.MIDDLEWARE, "Check if 'SecurityMiddleware' is in MIDDLEWARE"

def test_root_urlconf():
    assert settings.ROOT_URLCONF == 'webapp.urls', "Check if ROOT_URLCONF is set to 'webapp.urls'"

def test_templates():
    assert settings.TEMPLATES[0]['BACKEND'] == 'django.template.backends.django.DjangoTemplates', "Check if the template backend is set to DjangoTemplates"

def test_wsgi_application():
    assert settings.WSGI_APPLICATION == 'webapp.wsgi.application', "Check if WSGI_APPLICATION is set to 'webapp.wsgi.application'"

def test_database_default():
    assert settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3', "Check if default database engine is sqlite3"

def test_language_code():
    assert settings.LANGUAGE_CODE == 'en-us', "Check if LANGUAGE_CODE is set to 'en-us'"

def test_time_zone():
    assert settings.TIME_ZONE == 'UTC', "Check if TIME_ZONE is set to 'UTC'"

def test_use_i18n():
    assert settings.USE_I18N is True, "Check if USE_I18N is set to True"

def test_use_tz():
    assert settings.USE_TZ is True, "Check if USE_TZ is set to True"

def test_static_url():
    assert settings.STATIC_URL == 'static/', "Check if STATIC_URL is set to 'static/'"

def test_default_auto_field():
    assert settings.DEFAULT_AUTO_FIELD == 'django.db.models.BigAutoField', "Check if DEFAULT_AUTO_FIELD is set to 'django.db.models.BigAutoField'"