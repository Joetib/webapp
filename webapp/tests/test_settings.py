# test_settings.py
import pytest
from django.conf import settings

@pytest.mark.django_db
def test_debug_setting():
    assert settings.DEBUG is True, "DEBUG should be set to True in test settings"

@pytest.mark.django_db
def test_secret_key_setting():
    assert settings.SECRET_KEY == 'django-insecure-m#*+c#=%80gsv1ddca91&2u!za@5cfrpx@b-_e&%^1t%c#2zh_', "SECRET_KEY should be set to the expected value"

@pytest.mark.django_db
def test_allowed_hosts_setting():
    assert settings.ALLOWED_HOSTS == ['*'], "ALLOWED_HOSTS should allow all hosts"

@pytest.mark.django_db
def test_installed_apps_setting():
    assert "pages" in settings.INSTALLED_APPS, "The 'pages' app should be installed"

@pytest.mark.django_db
def test_middleware_setting():
    assert 'django.middleware.security.SecurityMiddleware' in settings.MIDDLEWARE, "SecurityMiddleware should be in MIDDLEWARE"

@pytest.mark.django_db
def test_templates_setting():
    assert settings.TEMPLATES[0]['BACKEND'] == 'django.template.backends.django.DjangoTemplates', "DjangoTemplates should be the template backend"

@pytest.mark.django_db
def test_wsgi_application_setting():
    assert settings.WSGI_APPLICATION == 'webapp.wsgi.application', "WSGI_APPLICATION should be set to 'webapp.wsgi.application'"

@pytest.mark.django_db
def test_database_default_setting():
    assert settings.DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3', "Default database engine should be sqlite3"

@pytest.mark.django_db
def test_language_code_setting():
    assert settings.LANGUAGE_CODE == 'en-us', "LANGUAGE_CODE should be set to 'en-us'"

@pytest.mark.django_db
def test_time_zone_setting():
    assert settings.TIME_ZONE == 'UTC', "TIME_ZONE should be set to 'UTC'"

@pytest.mark.django_db
def test_use_i18n_setting():
    assert settings.USE_I18N is True, "USE_I18N should be set to True"

@pytest.mark.django_db
def test_use_tz_setting():
    assert settings.USE_TZ is True, "USE_TZ should be set to True"

@pytest.mark.django_db
def test_static_url_setting():
    assert settings.STATIC_URL == 'static/', "STATIC_URL should be set to 'static/'"

@pytest.mark.django_db
def test_default_auto_field_setting():
    assert settings.DEFAULT_AUTO_FIELD == 'django.db.models.BigAutoField', "DEFAULT_AUTO_FIELD should be set to 'django.db.models.BigAutoField'"
