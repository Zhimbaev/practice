-- удаляем старые версии процедур/функции
DROP PROCEDURE IF EXISTS add_phone(varchar, varchar, varchar);
DROP PROCEDURE IF EXISTS move_to_group(varchar, varchar);
DROP FUNCTION IF EXISTS search_contacts(text);

----------------------------------------------------
-- ДОБАВЛЕНИЕ ТЕЛЕФОНА К КОНТАКТУ
----------------------------------------------------
CREATE OR REPLACE PROCEDURE add_phone(
    p_name VARCHAR,
    p_phone VARCHAR,
    p_type VARCHAR  -- home / work / mobile
)
LANGUAGE plpgsql
AS $$
DECLARE
    contact_id INT;
BEGIN
    -- ищем контакт по имени
    SELECT id INTO contact_id
    FROM contacts
    WHERE name = p_name;

    -- если не нашли
    IF contact_id IS NULL THEN
        RAISE NOTICE 'Contact "%" not found', p_name;
        RETURN;
    END IF;

    -- добавляем номер
    INSERT INTO phones(contact_id, phone, type)
    VALUES (contact_id, p_phone, p_type);

    RAISE NOTICE 'Phone added for "%"', p_name;
END;
$$;


----------------------------------------------------
-- ПЕРЕНОС КОНТАКТА В ГРУППУ
----------------------------------------------------
CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_contact_id INT;
    v_group_id INT;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE name = p_contact_name;

    IF v_contact_id IS NULL THEN
        RAISE NOTICE 'Contact not found';
        RETURN;
    END IF;

    SELECT id INTO v_group_id
    FROM groups
    WHERE name = p_group_name;

    IF v_group_id IS NULL THEN
        INSERT INTO groups(name)
        VALUES (p_group_name)
        RETURNING id INTO v_group_id;
    END IF;

    UPDATE contacts
    SET group_id = v_group_id
    WHERE id = v_contact_id;
END;
$$;

----------------------------------------------------
-- ПОИСК КОНТАКТОВ (имя / email / телефон)
----------------------------------------------------
CREATE OR REPLACE FUNCTION search_contacts(p_text TEXT)
RETURNS TABLE (
    id INT,
    name VARCHAR,
    email VARCHAR,
    birthday DATE,
    group_name VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id,
        c.name,
        c.email,
        c.birthday,
        g.name
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE
        c.name ILIKE '%' || p_text || '%'
        OR c.email ILIKE '%' || p_text || '%'
        OR p.phone ILIKE '%' || p_text || '%';
END;
$$;