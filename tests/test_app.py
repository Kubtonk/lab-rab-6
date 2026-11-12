from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Cloud project is running in Docker!" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_not_found_endpoint():
    client = app.test_client()
    response = client.get("/non-existent-route")
    assert response.status_code == 404
