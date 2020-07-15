def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "<h1>Health check: up and running!</h1>"