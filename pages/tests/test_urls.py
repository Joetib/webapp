# test_urls.py
from django.urls import reverse, resolve
from pages import views
import pytest

@pytest.mark.django_db
def test_homepage_url():
    path = reverse('homepage')
    assert resolve(path).view_name == 'homepage'
    assert resolve(path).func == views.homepage