-- Import in hbtn_0c_0 database to the table.
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` WHERE `month` = 7 OR `month` = 8 GROUP BY `city` ORDER BY `avg_temp` DESC LIMIT 3;