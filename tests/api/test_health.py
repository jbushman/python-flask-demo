import pytest
from app import initialize_web_app


@pytest.fixture
def app():
    app = initialize_web_app()
    return app.app


def test_health_status(client):
    url = 'http://localhost:8000/api/health/status'

    resp = client.get(url)
    assert resp.status_code == 200

    resp_body = resp.json
    assert resp_body['successful'] is True
    assert resp_body['status'] == 'active'
