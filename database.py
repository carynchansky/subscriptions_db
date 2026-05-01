import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="subscription_tracker"
    )

def execute_query(query, params=None, fetch=False):
    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(query, params or ())
        if fetch:
            return cursor.fetchall()
        conn.commit()
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()