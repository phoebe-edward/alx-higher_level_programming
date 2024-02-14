-- create database and table inside it with FOREIGN KEY
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INTEGER UNIQUE AUTO_INCREMENT PRIMARY KEY, state_id INTEGER NOT NULL, FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id), name VARCHAR(256) NOT NULL);
