-- listing all records of the table which have a name value
-- orderd by desending order score
SELECT `score` , `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
