import json
from flask import Blueprint, jsonify, request

from project.models.obj import Obj

obj_controller = Blueprint('obj_controller', __name__)
@obj_controller.route('/api/objects', methods=['GET'])
def get_all_objects():
    objects = Obj.query.all()
    return jsonify(objects)