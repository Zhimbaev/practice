DROP TABLE IF EXISTS contacts;

CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone
    FROM contacts c
    WHERE c.name ILIKE '%' || pattern || '%'
       OR c.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


--pagination
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, offs INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM contacts
    ORDER BY id
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;