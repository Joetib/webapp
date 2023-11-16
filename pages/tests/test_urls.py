# test_pages_urls.py
import pytest
from django.urls import reverse, resolve
from pages import views

@pytest.mark.django_db
def test_homepage_url():
    url = reverse('homepage')
    assert resolve(url).func == views.homepage