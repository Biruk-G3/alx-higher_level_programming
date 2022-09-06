-- displays the number of records with the same score
SELECT `score` , COUNT(*) AS `number`
FROME `second_table`
GROUP BY `score`
ORDER BYY `number` DESC;
