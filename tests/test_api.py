"""Tests for Stock Price API"""

import json

import pytest

from api import app


@pytest.fixture
def _client():
    """Yields a test instance of the API

    Every test will be run within this context"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


################## VALID CASES ##########################################


def test_valid_request(_client):
    """Make a request with a valid instrument symbol"""
    resp = _client.get("/?symbol=CAT")
    assert resp.status_code == 200
    data = json.loads(resp.get_data().decode('utf-8').replace("'", '"'))
    assert data.get("currency") == "$"
    assert data.get("symbol") == "CAT"
    assert isinstance(data.get("price"), float)


def test_valid_request_unknown_symbol(_client):
    """Make a request with an unkown instrument symbol"""
    resp = _client.get("/?symbol=UNKNOWN")
    assert resp.status_code == 200
    data = json.loads(resp.get_data().decode('utf-8').replace("'", '"'))
    assert not any(data)


################## ERROR CASES ##########################################


def test_missing_symbol_parameter(_client):
    """Make a request with no symbol parameter"""
    resp = _client.get("/")
    assert resp.status_code == 200
    data = json.loads(resp.get_data().decode('utf-8').replace("'", '"'))
    assert data["message"].startswith("The URL must include a symbol parameter")

    resp = _client.get("/?arg=random")
    assert resp.status_code == 200
    data = json.loads(resp.get_data().decode('utf-8').replace("'", '"'))
    assert data["message"].startswith("The URL must include a symbol parameter")
