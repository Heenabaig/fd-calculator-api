from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json() == {"status": "ok"}

def test_calculate():
    r = client.post("/calculate", json={"principal": 100000, "rate": 7, "years": 1})
    assert r.status_code == 200
    assert r.json()["maturity_amount"] > 999999