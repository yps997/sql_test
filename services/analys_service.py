from sqlalchemy import text
from models.DB import db


def get_attack_analysis(year):
    query = text("""
        SELECT 
            m.air_force,
            l.target_city,
            COUNT(*) AS mission_count
        FROM mission m 
        INNER JOIN  location l ON m.location_id = l.location_id
        WHERE EXTRACT(YEAR FROM mission_date) = :year
        GROUP BY air_force, target_city
        ORDER BY mission_count DESC
        LIMIT 1;
    """)
    result = db.session.execute(query, {'year': year})
    data = result.fetchone()
    if data:
        return {
            'air_force': data['air_force'],
            'target_city': data['target_city'],
            'mission_count': data['mission_count']
        }
    else:
        return None