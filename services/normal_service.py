import psycopg2

def normalize_db():
    target_conn = psycopg2.connect(
        dbname="wwi_missions",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
    return target_conn

#     try:
#         cur = target_conn.cursor()
#
#         # Query 1: Create Target Locations table
#         query1 = """
#         CREATE TABLE Locations
# (
#     Id SERIAL PRIMARY KEY,
#     City VARCHAR(100),
#     Country VARCHAR(100),
#     Lon FLOAT,
#     Lat FLOAT,
#     UNIQUE (Country, City, Lon, Lat)
# );
#         """
#         cur.execute(query1)
#
#         # Query 2: Add Target_location column to mission table
#         query2 = """
#         ALTER TABLE Mission
#     ADD COLUMN IF NOT EXISTS target_location INTEGER REFERENCES Locations(id);
#         """
#         cur.execute(query2)
#
#         # Query 3: Insert data into Locations and update mission table
#         query3 = """
#         INSERT INTO Locations (country, city, lat, lon)
# SELECT DISTINCT target_country, target_city, target_latitude, target_longitude
# FROM Mission
# WHERE target_country IS NOT NULL
#   AND target_city IS NOT NULL
#   AND target_latitude IS NOT NULL
#   AND target_longitude IS NOT NULL
# ON CONFLICT (country, city, lat, lon) DO NOTHING;
#         """
#         cur.execute(query3)
#
#         # Query4: Update Mission table with corresponding location ids
#         query4 = """UPDATE Mission m
# SET target_location = l.id
# FROM Locations l
# WHERE m.target_country = l.country
#   AND m.target_city = l.city
#   AND m.target_longitude = l.lon
#   AND m.target_latitude = l.lat;
# """
#         cur.execute(query4)
#
#
#         # Query5: Drop unnecessary columns from mission table
#         query5 = """
#         ALTER TABLE mission
#         DROP COLUMN IF EXISTS target_city,
#         DROP COLUMN IF EXISTS target_country,
#         DROP COLUMN IF EXISTS target_longitude,
#         DROP COLUMN IF EXISTS target_latitude;
#         """
#         cur.execute(query5)
#
#     finally:
#         target_conn.close()
#
#






if __name__ == "__main__":
    normalize_db()