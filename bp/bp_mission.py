from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
#from models import Mission, db

mission_bp = Blueprint('users', __name__)

@mission_bp.route('/api/mission', methods=['GET'])
def get_missions():
    missions = get_missions()
    if missions:
        return jsonify([mission.to_dict() for mission in missions]), 200
    else:
        return jsonify(f'not found any mission in the database')
@mission_bp.route('/api/mission/<int:id>', methods=['GET'])
def get_mission(id):
    mission = get_mission(id)
    if mission:
        return jsonify(mission.to_dict()), 200
    else:
        return jsonify({'error': 'Mission not found'}), 404