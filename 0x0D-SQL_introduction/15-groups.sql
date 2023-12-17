-- select from table those with the same score and count them
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
