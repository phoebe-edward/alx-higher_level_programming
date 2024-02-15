-- select all cities and mention their states by joining the two tables cities and states
SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id;

