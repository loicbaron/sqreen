import json
import os
from flask import jsonify

def test_notifications_without_signature_forbidden(client):
    rv = client.post('/api/notifications', json={
        'test': 'will be forbidden'
    })
    json_data = rv.get_json()
    assert rv.status_code == 403

def test_notifications_signature_ok(client):
    req_sig = '9d101d2bf630748679226b767d2031634c520390ff0e926afc09bc65a05bfdb2'
    rv = client.post(
        '/api/notifications', 
        headers={'X-Sqreen-Integrity': req_sig},
        data='4567'
    )
    json_data = rv.get_json()
    assert rv.status_code == 200
    
