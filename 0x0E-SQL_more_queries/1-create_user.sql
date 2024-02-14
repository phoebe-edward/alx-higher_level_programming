-- create user if he does not exist and grant him all privilages
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY '1-create_user.sql';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
