-- Lists all records with a score >= 10 in the table.
SELECT `score`, `name` >= 10 FROM `second_table` ORDER BY `score` DESC;