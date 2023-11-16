# test_apps.py
from django.apps import apps
from pages.apps import PagesConfig
import pytest

@pytest.mark.django_db
def test_apps():
    assert PagesConfig.name == 'pages'
    assert apps.get_app_config('pages').name == 'pages'