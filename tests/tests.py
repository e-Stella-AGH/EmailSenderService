from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_send_email_with_dry_run():
    response = client.post(
        "/email",
        headers={"X-Dry-Run": "True"},
        json={
            "subject": "str",
            "receiver": "str",
            "content": "str"
        },)
    assert response.status_code == 200
    assert response.json() == {
        'mail': {
            "subject": "str",
            "receiver": "str",
            "content": "str",
            "sender_email": "no-reply@e-stella.com",
            "sender_name": "No Reply"
        }
    }
