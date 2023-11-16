from django.test import TestCase, Client
from django.urls import reverse

class HomePageViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_homepage_view_status_code(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_view_template_used(self):
        response = self.client.get(reverse('homepage'))
        self.assertTemplateUsed(response, 'homepage.html')

    def test_homepage_view_content(self):
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, "Welcome to the homepage")