import psycopg2
import csv
from config import host, user, password, db_name

try:
    # Connect to the existing database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True
    
    # Checking server version
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")
    
    # Creating a new table
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS users;")
        cursor.execute("""
            CREATE TABLE users (
                id serial PRIMARY KEY,
                name varchar(50) NOT NULL,
                phone_number varchar(50) NOT NULL
            )
        """)
        print(f"[INFO] Table created successfully")

    # Inserting data into the table
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO users (name, phone_number) VALUES (%s, %s)",
            ("John", "1234567890")
        )
        print(f"[INFO] Data was successfully inserted")

    # Querying data from the table
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM users WHERE name = 'John'"
        )
        print(cursor.fetchone())

    # Deleting a record from the table
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM users WHERE name = 'John'"
        )
        print("[INFO] Record deleted successfully")

    # Updating data in the table
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE users SET phone_number = '0987654321' WHERE name = 'Alice'"
        )
        print("[INFO] Data updated successfully")

except Exception as ex:
    print("[INFO] Error while working with PostgreSQL:", ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
