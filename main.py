from database import execute_query

# Displays the main menu options to the user
def menu():
    print("\n--- Subscription Tracker ---")
    print("1. Add Subscription")
    print("2. View Subscriptions")
    print("3. Update Subscription")
    print("4. Delete Subscription")
    print("5. Exit")

# Gets all valid payment method IDs from the database
def get_payment_ids():
    rows = execute_query("SELECT payment_id FROM PaymentMethods", fetch=True)
    return [r[0] for r in rows]  # Extract only the ID values from query result

# Adds a new subscription to the database
def add_subscription():
    name = input("Name: ")

    # Validate cost input
    try:
        cost = float(input("Cost: "))
    except:
        print("Invalid cost!")
        return

    # Validate payment method input
    try:
        payment_id = int(input("PaymentID: "))
    except:
        print("Invalid Payment Method!")
        return

    # Check if payment ID exists in database
    valid_ids = get_payment_ids()

    if payment_id not in valid_ids:
        print("Payment ID does not exist!")
        print("Valid IDs:", valid_ids)
        return

    # Insert new subscription into database
    query = "INSERT INTO Subscriptions (name, cost, payment_id) VALUES (%s, %s, %s)"
    execute_query(query, (name, cost, payment_id))

    print("Added!")

# Displays all subscriptions from the database
def view_subscriptions():
    rows = execute_query("SELECT * FROM Subscriptions", fetch=True)

    print("\n--- Subscriptions ---")
    for r in rows:
        print(r)

# Updates an existing subscription
def update_subscription():
    sub_id = input("ID: ")

    # Validate new cost input
    try:
        new_cost = float(input("New cost: "))
    except:
        print("Invalid number!")
        return
    
    # Validate new payment method input
    try:
        new_payment_id = int(input("New PaymentID: "))
    except:
        print("Invalid Payment Method!")
        return

    # Update record in database
    query = "UPDATE Subscriptions SET cost=%s, payment_id=%s WHERE subscription_id=%s"
    execute_query(query, (new_cost, new_payment_id, sub_id))

    print("Updated!")

# Deletes a subscription after confirmation
def delete_subscription():
    sub_id = input("ID: ")

    # Ask user for confirmation before deleting
    confirm = input("Are you sure? (y/n): ")
    if confirm.lower() == 'y':
        execute_query(
            "DELETE FROM Subscriptions WHERE subscription_id=%s",
            (sub_id,)
        )
        print("Deleted.")
    else:
        print("Cancelled.")

# Main program loop
def main():
    while True:
        menu()
        choice = input("Choose: ")

        # Handle user selection
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


# Runs the program only if this file is executed directly
if __name__ == "__main__":
    main()