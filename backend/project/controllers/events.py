import json
from dataclasses import asdict
from flask import Blueprint, jsonify, request

from project.models.event import Event

events_controller = Blueprint('events_controller', __name__)
@events_controller.route('/api/events', methods=['GET'])
def get_all_events():
    events = Event.query.all()
    return jsonify([asdict(event) for event in events])