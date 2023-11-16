from django.test import TestCase
from pages.apps import PagesConfig

class PagesConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(PagesConfig.name, 'pages')
        self.assertEqual(PagesConfig.default_auto_field, 'django.db.models.BigAutoField')