-- a script that lists all records of the table second_table of the database
SELECT score, name WHERE name IS NOT NULL FROM second_table ORDER BY score DESC, name;
