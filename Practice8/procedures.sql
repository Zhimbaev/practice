--Upsert (insert или update)
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone)
        VALUES(p_name, p_phone);
    END IF;
END;
$$;

--Delete по имени ИЛИ телефону
CREATE OR REPLACE PROCEDURE delete_contact(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p_value OR phone = p_value;
END;
$$;

--Bulk insert 
CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    names TEXT[],
    phones TEXT[],
    OUT invalid_data TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(names, 1)
    LOOP
        -- телефон должен быть только из цифр и длина 11
        IF phones[i] ~ '^[0-9]{11}$' THEN
            CALL upsert_contact(names[i], phones[i]);
        ELSE
            invalid := array_append(invalid, names[i] || ':' || phones[i]);
        END IF;
    END LOOP;

    invalid_data := invalid;
END;
$$;