import json
from flask import Blueprint, current_app, jsonify, request
from concurrent.futures import ThreadPoolExecutor

from project.config.security import verify_request_signature
from project.models.event import Event
from project.config.database import db_session
from project.notifications.dispatcher import dispatch

notifications_controller = Blueprint('notifications_controller', __name__)
@notifications_controller.route('/api/notifications', methods=['POST'])
@verify_request_signature
def post_notifications():
    # todo: sanitize JSON to avoid injections
    json_data = request.get_json()
    if not isinstance(json_data, list):
        json_data = [json_data]
    for event in json_data:
        process_event(event)
    return jsonify({'status': 'running'})

def process_event(event):
    if isinstance(event, str):
        data = json.loads(event)
    else:
        data = event
    # validate data format
    event = Event.fromBlob(data)
    # save to DB
    # todo: extract into a repository
    db_session.add(event)
    db_session.commit()
    # using a Thread to run tasks in background
    # todo: distribute tasks to workers
    #       use Celery Or send the task to a Queue (Reddis, ZMQ...)
    executor = ThreadPoolExecutor(1)
    workers = current_app.config['WORKERS']
    executor.submit(dispatch, message=str(event), workers=workers)