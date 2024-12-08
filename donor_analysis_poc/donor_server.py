import psycopg2

DATABASE_URL = "postgresql://admin:JAc6pXCdY0vMQzOHGKonb2O3zpdNXd4R@dpg-ct95fdl6l47c73an6bpg-a.oregon-postgres.render.com/donordb"

try:
    # Establish the connection using the URL
    connection = psycopg2.connect(DATABASE_URL)
    print("Connected to the database successfully!")

    # Test query
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    print(f"Database version: {cursor.fetchone()}")

    cursor.close()
    connection.close()

except Exception as e:
    print(f"Error: {e}")
