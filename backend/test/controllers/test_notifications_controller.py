import json
import os
from flask import jsonify
from unittest.mock import patch

from project.notifications.notify_email import NotifyEmail
from test.models.test_event import ev

def test_notifications_without_signature_forbidden(client):
    rv = client.post('/api/notifications', json={
        'test': 'will be forbidden'
    })
    json_data = rv.get_json()
    assert rv.status_code == 403

def get_true():
    return True

def test_notifications_bad_user_input(client, mocker):
    mocker.patch("project.config.security.check_signature", return_value=True)
    req_sig = '9d101d2bf630748679226b767d2031634c520390ff0e926afc09bc65a05bfdb2'
    rv = client.post(
        '/api/notifications', 
        headers={'X-Sqreen-Integrity': req_sig},
        data='4567'
    )
    assert rv.status_code == 500

def test_notifications_wrong_message_format(client, mocker):
    message = {'id': 4567, 'attribute': 'abc'}
    mocker.patch("project.config.database.db_session.add", return_value=True)
    mocker.patch("project.config.database.db_session.commit", return_value=True)
    mocker.patch("project.config.security.check_signature", return_value=True)
    req_sig = '9d101d2bf630748679226b767d2031634c520390ff0e926afc09bc65a05bfdb2'
    rv = client.post(
        '/api/notifications', 
        headers={'X-Sqreen-Integrity': req_sig},
        json=json.dumps(message)
    )
    json_data = rv.get_json()
    assert rv.status_code == 500

def test_notifications_ok(client, mocker):
    mocker.patch("project.config.database.db_session.add", return_value=True)
    mocker.patch("project.config.database.db_session.commit", return_value=True)
    mocker.patch("project.config.security.check_signature", return_value=True)
    req_sig = '9d101d2bf630748679226b767d2031634c520390ff0e926afc09bc65a05bfdb2'
    rv = client.post(
        '/api/notifications', 
        headers={'X-Sqreen-Integrity': req_sig},
        json=json.dumps(ev)
    )
    json_data = rv.get_json()
    assert rv.status_code == 200
