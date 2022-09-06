-- Display the avrage temprature (in Farhanite)
-- by city order descending tepreture
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
