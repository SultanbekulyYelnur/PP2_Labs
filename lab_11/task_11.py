import psycopg2

# DB Connection
def connect():
    return psycopg2.connect(
        dbname="phonebook_db11",      
        user="postgres",
        password="AlSanBek12",
        host="localhost",
        port="5432"
    )

# 1. Search by Pattern
def search_contacts(pattern):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
            rows = cur.fetchall()
            print("\nSearch Results:")
            for row in rows:
                print(row)

# 2. Insert or Update Single User
def insert_or_update_user(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
            conn.commit()
            print("✅ User inserted or updated.")

# 3. Insert Many Users
def insert_many_users(names, phones):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM insert_many_users(%s, %s);", (names, phones))
            invalid_rows = cur.fetchall()
            if invalid_rows:
                print("Invalid entries returned:")
                for row in invalid_rows:
                    print(f"Name: {row[0]}, Phone: {row[1]}, Reason: {row[2]}")
            else:
                print("All users inserted successfully.")

                
# 4. Pagination Query
def get_contacts(limit_val, offset_val):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_contacts(%s, %s);", (limit_val, offset_val))
            rows = cur.fetchall()
            print("\nPaginated Contacts:")
            for row in rows:
                print(row)

#  5. Delete User by Name or Phone
def delete_user(value, by):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_user(%s, %s);", (value, by))
            conn.commit()
            print(f"Deleted user by {by}: {value}")

#  Sample CLI Menu
def menu():
    while True:
        print("\n📱 PhoneBook Menu")
        print("1. Search Contacts")
        print("2. Insert or Update User")
        print("3. Insert Many Users")
        print("4. Show Contacts (Paginated)")
        print("5. Delete User")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            pattern = input("Enter pattern to search: ")
            search_contacts(pattern)
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, phone)
        elif choice == "3":
            names = input("Enter comma-separated names: ").split(",")
            phones = input("Enter comma-separated phones: ").split(",")
            names = [n.strip() for n in names]
            phones = [p.strip() for p in phones]
            insert_many_users(names, phones)
        elif choice == "4":
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            get_contacts(limit, offset)
        elif choice == "5":
            val = input("Enter value (name or phone): ")
            by = input("Delete by 'name' or 'phone': ")
            delete_user(val, by)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()

