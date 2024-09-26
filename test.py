# from postgres_proj.db import get_db_connection
import psycopg2

def normalize_db():
    # source_conn = get_db_connection()
    target_conn = psycopg2.connect(
        dbname="wwi_missions",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    try :
        query1 = """
           CREATE TABLE Locations
(
    Id SERIAL PRIMARY KEY,
    City VARCHAR(30),
    Country VARCHAR(30),
    Lon FLOAT,
    Lat FLOAT,
    UNIQUE (Country, City, Lon, Lat)
);
        """

        query2 = """
        INSERT INTO Locations (City, Country, Lon, Lat)
SELECT DISTINCT ON (City, Country) City, Country, Lon, Lat
FROM operations
WHERE City IS NOT NULL
  AND Country IS NOT NULL
ON CONFLICT (City, Country) DO NOTHING;
        """



        # execute the queries
        cur = target_conn.cursor()
        cur.executemany([query1,])
        target_conn.commit()

        s_cur = source_conn.cursor()
        s_cur.execute("SELECT * FROM customers")
        while True:
            customer_row = s_cur.fetchone()
            if customer_row is None:
                break

            customer_name = customer_row[1]
            address = customer_row[3]
            city = customer_row[4]
            phone_numbers = customer_row[2].split(",")

            cur.execute("INSERT INTO customers (customer_name, address, city)"
                        " VALUES (%s, %s, %s) RETURNING customer_id",
                        (customer_name, address, city))
            customer_id = cur.fetchone()[0]

            for phone_number in phone_numbers:
                cur.execute("INSERT INTO phone_numbers (customer_id, phone_number)"
                            " VALUES (%s, %s)", (customer_id, phone_number))





    except Exception as e:
        pass
    finally:
        pass
