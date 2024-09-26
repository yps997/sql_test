import psycopg2

def normalize_db():
    target_conn = psycopg2.connect(
        dbname="wwi_missions",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    try:
        cur = target_conn.cursor()

        # Query 1: Create Target Locations table
        query1 = """
        CREATE TABLE IF NOT EXISTS Locations
        (
            Id SERIAL PRIMARY KEY,
            City VARCHAR(30),
            Country VARCHAR(30),
            Lon FLOAT,
            Lat FLOAT,
            UNIQUE (Country, City, Lon, Lat)
        );
        """
        cur.execute(query1)

        # Query 2: Add Target_location column to mission table
        query2 = """
        ALTER TABLE mission
        ADD COLUMN IF NOT EXISTS Target_location INTEGER;
        """
        cur.execute(query2)

        # Query 3: Insert data into Locations and update mission table
        query3 = """
        WITH inserted_locations AS (
            INSERT INTO Locations (City, Country, Lon, Lat)
            SELECT DISTINCT ON (target_city, target_country) 
                   target_city, target_country, target_longitude, target_latitude
            FROM mission
            WHERE target_city IS NOT NULL
              AND target_country IS NOT NULL
            ON CONFLICT (City, Country) DO UPDATE
            SET Lon = EXCLUDED.Lon, Lat = EXCLUDED.Lat
            RETURNING Id, City, Country
        )
        UPDATE mission
        SET Target_location = inserted_locations.Id
        FROM inserted_locations
        WHERE mission.target_city = inserted_locations.City
          AND mission.target_country = inserted_locations.Country;
        """
        cur.execute(query3)

        # Query 4: Drop unnecessary columns from mission table
        query4 = """
        ALTER TABLE mission
        DROP COLUMN IF EXISTS target_city,
        DROP COLUMN IF EXISTS target_country,
        DROP COLUMN IF EXISTS target_longitude,
        DROP COLUMN IF EXISTS target_latitude;
        """
        cur.execute(query4)

        # Commit the changes
        target_conn.commit()



    except Exception as e:
        print(f"An error occurred: {e}")
        target_conn.rollback()
    finally:
        if cur:
            cur.close()
        if target_conn:
            target_conn.close()

if __name__ == "__main__":
    normalize_db()