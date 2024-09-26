from bp.bp_mission import mission_bp as db

class Mission(db.Model):
    __tablename__ = 'mission'
    mission_id = db.Column(db.Integer, primary_key=True)
    mission_date = db.Column(db.Date)
    theater_of_operations = db.Column(db.String(200))
    country = db.Column(db.String(200))
    air_force = db.Column(db.String(200))
    unit_id = db.Column(db.Integer)
    aircraft_series = db.Column(db.String(200))
    location_id = db.Column(db.Integer, foreign_key=True)

    def get_dict(self):
        return {
            'mission_id': self.mission_id,
            'mission_date': self.mission_date,
            'theater_of_operations': self.theater_of_operations,
            'country': self.country,
            'air_force': self.air_force,
            'unit_id': self.unit_id,
            'aircraft_series': self.aircraft_series
        }


class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.Integer, primary_key=True)
    loc_country = db.Column(db.String(200))
    loc_city = db.Column(db.String(200))
    loc_lat = db.Column(db.Float)
    loc_lon = db.Column(db.Float)

    def get_dict(self):
        return {
            'location_id': self.location_id,
            'loc_country': self.loc_country,
            'loc_city': self.loc_city,
            'loc_lat': self.loc_lat,
            'loc_lon': self.loc_lon
        }



