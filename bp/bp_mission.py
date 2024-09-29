from flask import Blueprint, jsonify
import psycopg2
from services.mission_service import get_missions, get_mission_by_id
from services.normal_service import normalize_db
from models.mission_models import Mission
mission_bp = Blueprint('mission', __name__)

@mission_bp.route('/m', methods=['GET'])
def list_missions():
    con = normalize_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM mission')
    my_list = []
    for i in range(10):
        missions = cur.fetchone()
        new_mission = Mission(mission_date=missions[1],theater_of_operations=missions[2]
                              ,country=missions[3],air_force=missions[4],
                              unit_id=missions[5],aircraft_series=missions[6],location_id=missions[13])
        mis =new_mission.get_dict()
        my_list.append(mis)
    if my_list:
        return jsonify(my_list), 200
    else:
        return jsonify({'message': 'No missions found in database'}), 404


@mission_bp.route('/<int:id>', methods=['GET'])
def get_mission(id):
    con = normalize_db()
    cur = con.cursor()
    cur.execute('SELECT * FROM mission WHERE mission_id = %s', (id,))
    mission_data = cur.fetchone()
    cur.close()
    con.close()

    if mission_data:
        mission = Mission(mission_date=mission_data[1],
                          theater_of_operations=mission_data[2],
                          country=mission_data[3],
                          air_force=mission_data[4],
                          unit_id=mission_data[5],
                          aircraft_series=mission_data[6],
                          location_id=mission_data[13])
        return jsonify(mission.get_dict()), 200
    else:
        return jsonify({'error': 'Mission not found'}), 404