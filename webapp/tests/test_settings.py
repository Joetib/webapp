# test_settings.py
import unittest
from django.conf import settings

class TestSettings(unittest.TestCase):

    def test_debug(self):
        self.assertTrue(settings.DEBUG)

    def test_secret_key(self):
        self.assertTrue(settings.SECRET_KEY)

    def test_allowed_hosts(self):
        self.assertIn('*', settings.ALLOWED_HOSTS)

    def test_installed_apps(self):
        self.assertIn('django.contrib.admin', settings.INSTALLED_APPS)

    def test_middleware(self):
        self.assertIn('django.middleware.security.SecurityMiddleware', settings.MIDDLEWARE)

    def test_root_urlconf(self):
        self.assertEqual(settings.ROOT_URLCONF, 'webapp.urls')

    def test_templates(self):
        self.assertIsInstance(settings.TEMPLATES, list)

    def test_wsgi_application(self):
        self.assertEqual(settings.WSGI_APPLICATION, 'webapp.wsgi.application')

    def test_database_default(self):
        self.assertIn('default', settings.DATABASES)

    def test_auth_password_validators(self):
        self.assertIsInstance(settings.AUTH_PASSWORD_VALIDATORS, list)

    def test_language_code(self):
        self.assertEqual(settings.LANGUAGE_CODE, 'en-us')

    def test_time_zone(self):
        self.assertEqual(settings.TIME_ZONE, 'UTC')

    def test_use_i18n(self):
        self.assertTrue(settings.USE_I18N)

    def test_use_tz(self):
        self.assertTrue(settings.USE_TZ)

    def test_static_url(self):
        self.assertEqual(settings.STATIC_URL, 'static/')

    def test_default_auto_field(self):
        self.assertEqual(settings.DEFAULT_AUTO_FIELD, 'django.db.models.BigAutoField')

if __name__ == '__main__':
    unittest.main()