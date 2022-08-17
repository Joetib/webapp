from http import HTTPStatus
from django.test import TestCase

# Create your tests here.
class HomePageTestCase(TestCase):
    def test_homepage_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)