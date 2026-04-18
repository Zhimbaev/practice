from connect import get_connection
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added/updated.")

def search_contacts():
    pattern = input("Enter search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def get_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def delete_contact():
    value = input("Enter name or phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted.")


if __name__ == "__main__":
    while True:
        print("\nPractice 8 Test Menu")
        print("1. Search")
        print("2. Add/Upsert")
        print("3. Delete")
        print("4. Pagination")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search_contacts()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            get_paginated()
        elif choice == "0":
            break