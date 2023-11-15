# test for webapp/asgi.py
import pytest
from django.conf import settings
from channels.testing import HttpCommunicator
from webapp.asgi import application

@pytest.mark.asyncio
async def test_asgi_application():
    communicator = HttpCommunicator(application, "GET", "/")
    response = await communicator.get_response()
    assert response["status"] == 200