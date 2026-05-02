import csv
import json
from connect import get_connection


def create_tables():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        files = ["/Users/zamirzimbaev/Desktop/practice/TSIS1/schema.sql", "/Users/zamirzimbaev/Desktop/practice/TSIS1/procedures.sql"]

        for file in files:
            with open(file, encoding="utf-8") as f:
                sql = f.read().strip()
                if sql:
                    cur.execute(sql)

        conn.commit()
        print("Tables ready")

    except Exception as e:
        print("Error:", e)
        if conn:
            conn.rollback()

    finally:
        if cur: cur.close()
        if conn: conn.close()


def insert_console():
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        name = input("Name: ").strip()
        email = input("Email: ").strip() or None
        birthday = input("Birthday: ").strip() or None
        group = input("Group: ").strip() or None

        group_id = _get_group(cur, group) if group else None

        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING
            RETURNING id;
        """, (name, email, birthday, group_id))

        res = cur.fetchone()

        if not res:
            print("Contact exists")
            return

        contact_id = res[0]
        _add_phones(cur, contact_id)

        conn.commit()
        print("Saved")

    except Exception as e:
        print("Error:", e)

    finally:
        if cur: cur.close()
        if conn: conn.close()


def _add_phones(cur, contact_id):
    print("Phones (empty stop)")

    while True:
        phone = input("Phone: ").strip()
        if not phone:
            break

        ptype = input("Type: ").strip()
        if ptype not in ("home", "work", "mobile"):
            ptype = "mobile"

        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s, %s, %s)
        """, (contact_id, phone, ptype))


def _get_group(cur, name):
    cur.execute("SELECT id FROM groups WHERE name=%s", (name,))
    row = cur.fetchone()

    if row:
        return row[0]

    cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (name,))
    return cur.fetchone()[0]


def insert_csv(path):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for r in reader:
                name = r.get("name", "").strip()
                if not name:
                    continue

                email = r.get("email")
                birthday = r.get("birthday")
                group = r.get("group")

                group_id = _get_group(cur, group) if group else None

                cur.execute("""
                    INSERT INTO contacts(name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (name) DO NOTHING
                    RETURNING id;
                """, (name, email, birthday, group_id))

                res = cur.fetchone()

                if res and r.get("phone"):
                    cur.execute("""
                        INSERT INTO phones(contact_id, phone, type)
                        VALUES (%s, %s, %s)
                    """, (res[0], r["phone"], r.get("phone_type", "mobile")))

        conn.commit()
        print("CSV done")

    except Exception as e:
        print("Error:", e)

    finally:
        if cur: cur.close()
        if conn: conn.close()


def export_json(path="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT c.id, c.name, c.email, c.birthday, g.name
            FROM contacts c
            LEFT JOIN groups g ON g.id = c.group_id
        """)

        data = []

        for c in cur.fetchall():
            cid, name, email, birthday, group = c

            cur.execute("""
                SELECT phone, type FROM phones WHERE contact_id=%s
            """, (cid,))

            phones = [{"phone": p[0], "type": p[1]} for p in cur.fetchall()]

            data.append({
                "name": name,
                "email": email,
                "birthday": str(birthday),
                "group": group,
                "phones": phones
            })

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("Export done")

    finally:
        cur.close()
        conn.close()


def import_json(path="contacts.json"):
    conn = get_connection()
    cur = conn.cursor()

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        for c in data:
            name = c.get("name")

            cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
            exists = cur.fetchone()

            group_id = _get_group(cur, c.get("group")) if c.get("group") else None

            if exists:
                cur.execute("""
                    UPDATE contacts
                    SET email=%s, birthday=%s, group_id=%s
                    WHERE name=%s
                """, (c.get("email"), c.get("birthday"), group_id, name))

                cur.execute("DELETE FROM phones WHERE contact_id=%s", (exists[0],))
                cid = exists[0]

            else:
                cur.execute("""
                    INSERT INTO contacts(name, email, birthday, group_id)
                    VALUES (%s, %s, %s, %s)
                    RETURNING id
                """, (name, c.get("email"), c.get("birthday"), group_id))

                cid = cur.fetchone()[0]

            for p in c.get("phones", []):
                cur.execute("""
                    INSERT INTO phones(contact_id, phone, type)
                    VALUES (%s, %s, %s)
                """, (cid, p.get("phone"), p.get("type", "mobile")))

        conn.commit()
        print("JSON done")

    finally:
        cur.close()
        conn.close()


def call_add_phone():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("Phone: ")
    ptype = input("Type: ")

    cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()


def call_move_group():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    group = input("Group: ")

    cur.execute("CALL move_to_group(%s,%s)", (name, group))

    conn.commit()
    cur.close()
    conn.close()


def main():
    create_tables()

    while True:
        print("\n1 Insert")
        print("2 CSV")
        print("3 Export JSON")
        print("4 Import JSON")
        print("5 Add phone")
        print("6 Move group")
        print("0 Exit")

        c = input("> ")

        if c == "1":
            insert_console()
        elif c == "2":
            insert_csv("contacts.csv")
        elif c == "3":
            export_json()
        elif c == "4":
            import_json()
        elif c == "5":
            call_add_phone()
        elif c == "6":
            call_move_group()
        elif c == "0":
            break


if __name__ == "__main__":
    main()