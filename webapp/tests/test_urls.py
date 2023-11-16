# test_webapp_urls.py
from django.urls import reverse, resolve
from django.test import SimpleTestCase

class TestUrls(SimpleTestCase):

    def test_admin_url_resolves(self):
        url = reverse('admin:index')
        self.assertEquals(resolve(url).func.__name__, 'index')

    def test_homepage_url_resolves(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func.__name__, 'homepage')