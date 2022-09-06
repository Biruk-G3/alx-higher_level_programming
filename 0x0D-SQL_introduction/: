-- display the 3 citys with high temp avrage 
-- temp must happen b/n july and augest
SELECT `city` , AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3
