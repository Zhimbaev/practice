import csv
import psycopg2
from config import DB_CONFIG


def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn


def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            phone VARCHAR(20) UNIQUE
        );
    """)
    conn.commit()
    print("Таблица создана")
    cur.close()
    conn.close()


def insert_from_csv():
    conn = get_connection()
    cur = conn.cursor()
    with open("contacts.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO NOTHING;
            """, (row["first_name"], row["phone"]))
    conn.commit()
    print("Контакты из CSV загружены")
    cur.close()
    conn.close()


def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO phonebook (first_name, phone)
        VALUES (%s, %s)
        ON CONFLICT (phone) DO NOTHING;
    """, (name, phone))
    conn.commit()
    print("Контакт добавлен")
    cur.close()
    conn.close()


def update_contact():
    print("1 - Изменить имя")
    print("2 - Изменить телефон")
    choice = input("Выбор: ")
    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        old_name = input("Введите старое имя: ")
        new_name = input("Введите новое имя: ")
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s;", (new_name, old_name))

    elif choice == "2":
        old_phone = input("Введите старый телефон: ")
        new_phone = input("Введите новый телефон: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s;", (new_phone, old_phone))

    conn.commit()
    print("Контакт обновлен")
    cur.close()
    conn.close()


def search_contacts():
    print("1 - Показать всех")
    print("2 - Найти по имени")
    print("3 - Найти по номеру телефона")
    choice = input("Выбор: ")
    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT * FROM phonebook;")

    elif choice == "2":
        name = input("Введите имя: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s;", (f"%{name}%",))

    elif choice == "3":
        phone = input("Введите номер (или начало): ")
        cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s;", (f"{phone}%",))

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]}  Имя: {row[1]}  Телефон: {row[2]}")
    else:
        print("Ничего не найдено")

    cur.close()
    conn.close()


def delete_contact():
    print("1 - Удалить по имени")
    print("2 - Удалить по телефону")
    choice = input("Выбор: ")
    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        name = input("Введите имя: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))

    elif choice == "2":
        phone = input("Введите телефон: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))

    conn.commit()
    print("Контакт удален")
    cur.close()
    conn.close()


def main():
    create_table()

    while True:
        print("\n--- PhoneBook ---")
        print("1 - Загрузить из CSV")
        print("2 - Добавить контакт")
        print("3 - Обновить контакт")
        print("4 - Поиск")
        print("5 - Удалить контакт")
        print("0 - Выход")

        choice = input("Выбор: ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break


main()