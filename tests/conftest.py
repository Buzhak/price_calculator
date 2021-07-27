from flask import url_for
from webapp import create_app
import pytest 

@pytest.fixture
def app():
    app = create_app()
    return app

def test_app(client):
    assert client.get(url_for('index')).status_code == 200