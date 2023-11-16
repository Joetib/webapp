# test_views.py
import pytest
from django.urls import reverse
from django.test import RequestFactory
from pages import views

@pytest.mark.django_db
class TestViews:
    @classmethod
    def setup_method(cls):
        cls.factory = RequestFactory()

    def test_homepage_view(self):
        request = self.factory.get(reverse('homepage'))
        response = views.homepage(request)
        assert response.status_code == 200
        assert "homepage.html" in (t.name for t in response.templates)