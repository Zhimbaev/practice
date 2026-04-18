CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook (first_name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    v_name TEXT;
    v_phone TEXT;
BEGIN
    CREATE TEMP TABLE IF NOT EXISTS invalid_data (
        first_name TEXT,
        phone TEXT
    ) ON COMMIT DELETE ROWS;

    i := 1;
    WHILE i <= array_length(p_names, 1) LOOP
        v_name  := p_names[i];
        v_phone := p_phones[i];

        IF v_phone ~ '^\+[0-9]{7,15}$' THEN
            INSERT INTO phonebook (first_name, phone)
            VALUES (v_name, v_phone)
            ON CONFLICT (phone) DO NOTHING;
        ELSE
            INSERT INTO invalid_data (first_name, phone)
            VALUES (v_name, v_phone);
        END IF;

        i := i + 1;
    END LOOP;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name <> '' THEN
        DELETE FROM phonebook WHERE first_name = p_name;
    ELSE
        DELETE FROM phonebook WHERE phone = p_phone;
    END IF;
END;
$$;