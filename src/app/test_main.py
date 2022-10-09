import random
import string

from fastapi.testclient import TestClient

from app.main import app


def test_ping_pong():
    client = TestClient(app)

    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def generate_random_url() -> str:
    allowed_symbols = string.ascii_letters
    url_len = random.randint(4, 20)
    return "".join(random.choices(allowed_symbols, k=url_len)) + ".com"


def check_short_url_rules(short_url: str) -> bool:
    return (
        isinstance(short_url, str)
        and len(short_url) == 6
        and all(c in string.digits + string.ascii_letters for c in short_url)
    )


def test_create_get_delete():
    client = TestClient(app)

    fake_url = generate_random_url()
    response = client.post(f"/api/{fake_url}")
    assert response.status_code == 200
    assert response.json()["url"] == fake_url

    short_url = response.json()["short_url"]
    assert check_short_url_rules(short_url) == True

    response = client.get(f"/{short_url}")
    assert response.status_code == 200
    assert response.json() == {"url": fake_url, "short_url": short_url}

    response = client.put(f"/{short_url}")
    assert response.status_code == 200
    assert response.json() == {"url": fake_url, "short_url": short_url}

    response = client.get(f"/{short_url}")
    assert response.status_code == 404

    response = client.get(f"/{short_url}")
    assert response.status_code == 404
