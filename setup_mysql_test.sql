-- All your files should start by a comment describing the task
-- This script prepares a MySQL server for the project

-- If the user hbnb_test already exists, this will not fail
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';

-- Set the password for hbnb_test
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_test_pwd';

-- If the database hbnb_test_db already exists, this will not fail
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Apply the privileges
FLUSH PRIVILEGES;

