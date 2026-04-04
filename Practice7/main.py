# main.py
import csv
import os
from connect import get_conn, create_table

def from_csv(file_path):
    conn = get_conn()
    if not conn: return
    try:
        with open(file_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            with conn.cursor() as cur:
                for row in reader:
                    cur.execute(
                        "INSERT INTO contacts (username, first_name, phone) "
                        "VALUES (%s, %s, %s) ON CONFLICT DO NOTHING",
                        (row['username'], row['first_name'], row['phone'])
                    )
            conn.commit()
        print("Данные из CSV успешно импортированы.")
    except Exception as e:
        print(f"Ошибка импорта CSV: {e}")
    finally:
        conn.close()

def from_console():
    username = input("Введите уникальный username: ")
    first_name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    
    conn = get_conn()
    if not conn: return
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO contacts (username, first_name, phone) VALUES (%s, %s, %s)",
                (username, first_name, phone)
            )
        conn.commit()
        print("Контакт успешно добавлен.")
    except Exception as e:
        print(f"Не удалось добавить контакт: {e}")
    finally:
        conn.close()

def upd_contact():
    username = input("Введите username контакта для обновления: ")
    field = input("Что вы хотите обновить? (first_name/phone): ").lower()
    
    if field not in ['first_name', 'phone']:
        print("Ошибка: недопустимое поле.")
        return
        
    new_value = input(f"Введите новое значение для {field}: ")
    conn = get_conn()
    if not conn: return
    try:
        with conn.cursor() as cur:
            cur.execute(f"UPDATE contacts SET {field} = %s WHERE username = %s", (new_value, username))
            conn.commit()
            print("Данные успешно обновлены.")
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")
    finally:
        conn.close()

def search_contact():
    print("Фильтровать по: 1. Имени  2. Префиксу телефона  3. Показать всё")
    choice = input("> ")
    conn = get_conn()
    if not conn: return
    try:
        with conn.cursor() as cur:
            if choice == '1':
                name = input("Введите имя: ")
                cur.execute("SELECT * FROM contacts WHERE first_name ILIKE %s", (f"%{name}%",))
            elif choice == '2':
                prefix = input("Введите префикс номера: ")
                cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{prefix}%",))
            else:
                cur.execute("SELECT * FROM contacts")
            
            results = cur.fetchall()
            if not results:
                print("Ничего не найдено.")
            for row in results:
                print(row)
    finally:
        conn.close()

def del_contact():
    target = input("Введите username или номер телефона для удаления: ")
    conn = get_conn()
    if not conn: return
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM contacts WHERE username = %s OR phone = %s", (target, target))
            conn.commit()
            print("Запись удалена (если она существовала).")
    finally:
        conn.close()

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'contacts.csv')
    create_table()

    # Главное меню
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Импорт CSV\n2. Добавить контакт\n3. Обновить контакт\n4. Поиск\n5. Удалить\n6. Выход")
        cmd = input("Выберите опцию: ")
        
        if cmd == '1': from_csv(csv_path)
        elif cmd == '2': from_console()
        elif cmd == '3': upd_contact()
        elif cmd == '4': search_contact()
        elif cmd == '5': del_contact()
        elif cmd == '6': 
            print("Завершение работы.")
            break