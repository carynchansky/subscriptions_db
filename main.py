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

def menu():
    print("\n--- Subscription Tracker ---")
    print("1. Add Subscription")
    print("2. View Subscriptions")
    print("3. Update Subscription")
    print("4. Delete Subscription")
    print("5. Exit")

def get_payment_ids():
    rows = execute_query("SELECT payment_id FROM PaymentMethods", fetch=True)
    return [r[0] for r in rows]

def add_subscription():
    name = input("Name: ")

    try:
        cost = float(input("Cost: "))
    except:
        print("Invalid cost!")
        return

    try:
        payment_id = int(input("PaymentID: "))
    except:
        print("Invalid Payment Method!")
        return

    valid_ids = get_payment_ids()

    if payment_id not in valid_ids:
        print(" Payment ID does not exist!")
        print("Valid IDs:", valid_ids)
        return

    query = "INSERT INTO Subscriptions (name, cost, payment_id) VALUES (%s, %s, %s)"
    execute_query(query, (name, cost, payment_id))

    print("Added!")

def view_subscriptions():
    rows = execute_query("SELECT * FROM Subscriptions", fetch=True)

    print("\n--- Subscriptions ---")
    for r in rows:
        print(r)

def update_subscription():
    sub_id = input("ID: ")

    try:
        new_cost = float(input("New cost: "))
    except:
        print("Invalid number!")
        return
    
    try:
        new_payment_id = int(input("New PaymentID: "))
    except:
        print("Invalid Payment Method!")
        return

    query = "UPDATE Subscriptions SET cost=%s, payment_id=%s WHERE subscription_id=%s"
    execute_query(query, (new_cost, new_payment_id, sub_id))

    print("Updated!")

def delete_subscription():
    sub_id = input("ID: ")

    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        execute_query(
            "DELETE FROM Subscriptions WHERE subscription_id=%s",
            (sub_id,)
        )
        print("Deleted.")
    else:
        print("Cancelled.")

def main():
    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            add_subscription()
        elif choice == "2":
            view_subscriptions()
        elif choice == "3":
            update_subscription()
        elif choice == "4":
            delete_subscription()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()