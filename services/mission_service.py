from models.mission_models import Mission

def get_missions():
    missions = Mission.query.all()
    return [mission.to_dict() for mission in missions]

def get_mission_by_id(mission_id):
    mission = Mission.query.get(mission_id)
    if mission:
        return mission.to_dict()
    else:
        return None
