# test_pages_urls.py
import pytest
from django.urls import reverse, resolve
from pages import views

def test_homepage_url():
    path = reverse('homepage')
    assert resolve(path).func == views.homepage