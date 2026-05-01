import mysql.connector

# Creates and returns a connection to the MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",              # Database server (local machine)
        user="root",                   # MySQL username
        password="password",           # MySQL password (change if needed)
        database="subscription_tracker"  # Database name you're using
    )

# Executes SQL queries safely and handles connection/cleanup
def execute_query(query, params=None, fetch=False):
    # Open database connection
    conn = connect()
    cursor = conn.cursor()

    try:
        # Run SQL query with optional parameters
        cursor.execute(query, params or ())

        # If fetch=True, return results (SELECT queries)
        if fetch:
            return cursor.fetchall()

        # Save changes for INSERT/UPDATE/DELETE queries
        conn.commit()

    except Exception as e:
        # Print any SQL or connection errors
        print("Error:", e)

    finally:
        # Always close cursor and connection to free resources
        cursor.close()
        conn.close()