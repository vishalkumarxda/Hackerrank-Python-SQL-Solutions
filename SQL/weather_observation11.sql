SELECT DISTINCT city
FROM station
WHERE city not regexp '^[aeiou]' or city not regexp '[aeiou]$';