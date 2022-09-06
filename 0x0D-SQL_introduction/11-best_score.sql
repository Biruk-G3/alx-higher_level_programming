-- list all records from the table second_table
-- Records are ordered by score dscending
SELECT `score` , `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC
