from flask import Blueprint, jsonify
from services.mission_service import get_missions, get_mission_by_id

mission_bp = Blueprint('mission', __name__)

@mission_bp.route('/api/mission', methods=['GET'])
def get_missions():
    missions = get_missions()
    if missions:
        return jsonify(missions), 200
    else:
        return jsonify(f'not found mission in database')

@mission_bp.route('/api/mission/<int:id>', methods=['GET'])
def get_mission_bi_id():
    mission = get_mission_by_id(id)
    if mission:
        return jsonify(mission), 200
    else:
        return jsonify({'error': 'not found'}), 404


