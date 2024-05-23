-- Lists the number of records with the same score in the table second_table of the database.
SELECT COUNT(DISTINCT(`score`) AS `number` FROM `second_table` GROUP BY `score`;