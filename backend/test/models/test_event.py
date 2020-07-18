import json
from project.models.event import Event

ev = {
  "message_id": "86dea0ad-fd24-45e8-ab2c-5294c1221e1d",
  "api_version": "2",
  "date_created": "2020-07-17T22:33:26.287038+00:00",
  "message_type": "security_response",
  "retry_count": 0,
  "message": {
    "properties": {
      "ips": [
        {
          "ip_cidr": "127.0.0.1"
        }
      ],
      "user_identifiers": [
        "sqreen@example.com"
      ]
    },
    "application": {
      "name": "interview_backend",
      "id": "5f0ba429f1115100257ee352",
      "environment": "development"
    },
    "playbook": {
      "id": "5f1227366f5827016fd13e76",
      "name": "Test Playbook"
    }
  }
}

ev_without_id = {
  "message_id": None,
  "api_version": "2",
  "date_created": "2020-07-17T22:33:26.287038+00:00",
  "message_type": "security_response",
  "retry_count": 0,
  "message": {
    "properties": {
      "ips": [
        {
          "ip_cidr": "127.0.0.1"
        }
      ],
      "user_identifiers": [
        "sqreen@example.com"
      ]
    },
    "application": {
      "name": "interview_backend",
      "id": "5f0ba429f1115100257ee352",
      "environment": "development"
    },
    "playbook": {
      "id": "5f1227366f5827016fd13e76",
      "name": "Test Playbook"
    }
  }
}

def test_event_constructor():
  event = Event(
    ev['message_id'], 
    ev['api_version'], 
    ev['date_created'], 
    ev['message_type'], 
    ev['retry_count'], 
    ev['message']
  )
  assert isinstance(event, Event)
  assert event.message_id == "86dea0ad-fd24-45e8-ab2c-5294c1221e1d"

def test_event_fromBlob():
  event = Event.fromBlob(ev)
  assert isinstance(event, Event)
  assert event.message_id == "86dea0ad-fd24-45e8-ab2c-5294c1221e1d"

def test_event_fromBlob_id_none():
  event = Event.fromBlob(ev_without_id)
  assert isinstance(event, Event)
  assert event.message_id != None

def test_event_toJSON():
  json_event = Event.fromBlob(ev).toJSON()
  assert isinstance(json_event, str)
  assert json.loads(json_event)['message_id'] == "86dea0ad-fd24-45e8-ab2c-5294c1221e1d"

def test_event_str():
  event = Event.fromBlob(ev)
  assert "{}".format(event) == "message_id: {}, api_version: {}, date_created: {}, message_type: {}, retry_count: {}, message: {}"\
                              .format(event.message_id, event.api_version, event.date_created, event.message_type, event.retry_count, event.message)

def test_event_repr():
  event = Event.fromBlob(ev)
  assert repr(event) == "Event(message_id: {}, api_version: {}, date_created: {}, message_type: {}, retry_count: {}, message: {})"\
                              .format(event.message_id, event.api_version, event.date_created, event.message_type, event.retry_count, event.message)