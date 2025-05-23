-- this will run on Oracle

SELECT DISTINCT CITY 
FROM STATION 
WHERE MOD(ID, 2) = 0;


-- this will run on MySQLServer

SELECT DISTINCT CITY 
FROM STATION 
WHERE (ID % 2 = 0);