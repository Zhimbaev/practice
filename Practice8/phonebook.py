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
    cur.close()
    conn.close()
    print("таблица создана")


def load_sql_files():
    conn = get_connection()
    cur = conn.cursor()

    f = open("/Users/zamirzimbaev/Desktop/practice/Practice8/functions.sql", encoding="utf-8")
    sql = f.read()
    f.close()
    cur.execute(sql)

    f = open("/Users/zamirzimbaev/Desktop/practice/Practice8/procedures.sql", encoding="utf-8")
    sql = f.read()
    f.close()
    cur.execute(sql)

    conn.commit()
    cur.close()
    conn.close()
    print("скл файлы щагружены")


def search_by_pattern():
    pattern = input("введите часть имени или телефона: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print("ID:", row[0], " Имя:", row[1], " Телефон:", row[2])
    else:
        print("ничего не найдено")

    cur.close()
    conn.close()


def get_zapisi():
    limit = int(input("сколько записей показать: "))
    offset = int(input("пропустить сколько записей (0 = с начала): "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_zapisi(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print("ID:", row[0], "имя:", row[1], "телефон:", row[2])
    else:
        print("записей нет")

    cur.close()
    conn.close()


def upsert_contact():
    name = input("введите имя: ")
    phone = input("введите телефон: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("контакт добавлен или обновлён")


def insert_many():
    print("вводите контакты в формате: имя,телефон")
    print("когда закончите введите: с")

    names = []
    phones = []

    while True:
        line = input("имя,телефон: ")

        if line.lower() == "с":
            break

        parts = line.split(",")

        if len(parts) != 2:
            print("неверный формат, попробуйте снова")
            continue

        names.append(parts[0].strip())
        phones.append(parts[1].strip())

    if len(names) == 0:
        print("вы ничего не ввели")
        return

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many(%s, %s);", (names, phones))
    conn.commit()

    cur.execute("SELECT * FROM invalid_data;")
    bad_rows = cur.fetchall()

    if bad_rows:
        print("эти контакты не добавлены из за неверного телефона:")
        for row in bad_rows:
            print("имя:", row[0], "телефон:", row[1])
    else:
        print("все контакты успешно добавлены")

    cur.close()
    conn.close()


def delete_contact():
    print("1 - удалить по имени")
    print("2 - удалить по телефону")
    choice = input("Выбор: ")

    name = ""
    phone = ""

    if choice == "1":
        name = input("введите имя: ")
    elif choice == "2":
        phone = input("введите телефон: ")
    else:
        print("неверный выбор")
        return

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s, %s);", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("контакт удалён")


def main():
    create_table()
    load_sql_files()

    while True:
        print("\n меню:")
        print("1 - поиск")
        print("2 - показать")
        print("3 - добавить или обновить контакт")
        print("4 - удалить несколько")
        print("5 - удалить контакт")
        print("0 - стоп")

        choice = input("выбор: ")

        if choice == "1":
            search_by_pattern()
        elif choice == "2":
            get_zapisi()
        elif choice == "3":
            upsert_contact()
        elif choice == "4":
            insert_many()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break


main()