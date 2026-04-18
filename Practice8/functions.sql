CREATE OR REPLACE FUNCTION search_by_pattern(p TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.first_name, c.phone
        FROM phonebook c
        WHERE c.first_name ILIKE '%' || p || '%'
           OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_zapisi(lim INT, offs INT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT c.id, c.first_name, c.phone
        FROM phonebook c
        ORDER BY c.id
        LIMIT lim OFFSET offs;
END;    
$$ LANGUAGE plpgsql;