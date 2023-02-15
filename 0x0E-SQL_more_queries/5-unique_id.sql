-- a script that creates the table unique_id on your MySQL server
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE, name VARCHAR(256));
INSERT INTO unique_id VALUES(1)
