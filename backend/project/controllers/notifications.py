import json
from flask import Blueprint, jsonify, request
from concurrent.futures import ThreadPoolExecutor

from project.config.security import verify_request_signature
from project.notifications.dispatcher import dispatch

notifications_controller = Blueprint('notifications_controller', __name__)
@notifications_controller.route('/api/notifications', methods=['POST'])
@verify_request_signature
def post_notifications():
    # todo: sanitize JSON to avoid injections
    json_data = request.get_json()
    
    # using a Thread to run tasks in background
    # todo: distribute tasks to workers
    #       use Celery Or send the task to a Queue (Reddis, ZMQ...)
    executor = ThreadPoolExecutor(1)
    executor.submit(dispatch, message=json.dumps(json_data))
    return jsonify({'status': 'running'})