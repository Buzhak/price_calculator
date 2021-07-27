from flask.testing import FlaskClient
from flask import session, Flask
from webapp.calculator.forms import ItemForm


def test_index_endpoint(client: FlaskClient):
    res = client.get('/')
    assert res.status_code == 200