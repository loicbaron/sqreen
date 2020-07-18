from unittest.mock import patch
from project.models.event import Event

def test_get_all_objects(client):
  rv = client.get('/api/events')
  json_data = rv.get_json()
  assert rv.status_code == 200
  assert json_data == []