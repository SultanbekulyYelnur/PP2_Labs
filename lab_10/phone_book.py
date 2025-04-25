import psycopg2
import csv



# Database connection function
def connect():
    return psycopg2.connect(
        dbname="phones",     
        user="postgres",       
        password="AlSanBek12",   
        host="localhost",
        port="5432"
    )

    
    

# Create PhoneBook table
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            phone_number VARCHAR(20) UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# Insert from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    conn = connect()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO PhoneBook (first_name, phone_number) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Entry added successfully.")
    except psycopg2.Error as e:
        print("Error:", e)
    cur.close()
    conn.close()

# Insert from CSV
def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cur.execute("INSERT INTO PhoneBook (first_name, phone_number) VALUES (%s, %s)", 
                            (row['first_name'], row['phone_number']))
        conn.commit()
        print("CSV data inserted successfully.")
    except Exception as e:
        print("Error:", e)
    cur.close()
    conn.close()

# Update data by ID
def update_user():
    user_id = input("Enter user ID to update: ")
    new_name = input("Enter new name (or leave blank): ")
    new_phone = input("Enter new phone (or leave blank): ")
    
    conn = connect()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE PhoneBook SET first_name = %s WHERE id = %s", (new_name, user_id))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone_number = %s WHERE id = %s", (new_phone, user_id))
    conn.commit()
    print("User updated.")
    cur.close()
    conn.close()

# Query data
def query_users():
    filter_type = input("Filter by (name/phone/all): ").strip().lower()
    conn = connect()
    cur = conn.cursor()
    if filter_type == "name":
        name = input("Enter name to search: ")
        cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s", ('%' + name + '%',))
    elif filter_type == "phone":
        phone = input("Enter phone to search: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone_number = %s", (phone,))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    
    results = cur.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No matching records.")
    cur.close()
    conn.close()

# Delete user
def delete_user():
    method = input("Delete by (name/phone): ").strip().lower()
    value = input("Enter value to delete: ")
    
    conn = connect()
    cur = conn.cursor()
    if method == "name":
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (value,))
    elif method == "phone":
        cur.execute("DELETE FROM PhoneBook WHERE phone_number = %s", (value,))
    conn.commit()
    print("User deleted (if existed).")
    cur.close()
    conn.close()

# Main menu
def menu():
    create_table()  # Ensure table exists
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update user")
        print("4. Query users")
        print("5. Delete user")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            file_path = input("Enter CSV file path: ")
            insert_from_csv(file_path)
        elif choice == "3":
            update_user()
        elif choice == "4":
            query_users()
        elif choice == "5":
            delete_user()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()