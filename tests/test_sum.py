from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_sum_endpoint_returns_sum_of_query_params():
    response = client.get("/sum", params={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"sum": 5}
