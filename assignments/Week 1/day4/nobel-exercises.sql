-- SQL Exercises
-- --------------------
-- Use the nobel database from class to answer the following questions.

-- 1. Select the nobel database.

USE nobel;

-- 2. List the tables.

SHOW tables;

-- 3. Select the first ten records from the laureate table.

SELECT *
FROM laureate
LIMIT 10;

-- 4. Find the birth and death dates for Albert Einstein.

SELECT birth_date, death_date
FROM laureate
WHERE name='Albert Einstein';

-- 5. Find the Nobel Laureates who died in 2015 and whose name begins with 'Y'.

SELECT name, death_date
FROM laureate
WHERE (death_date LIKE '2015%') AND (name LIKE 'Y%')

-- 6. Find the last three Nobel Laureates born in 1900.

SELECT name, birth_date
FROM laureate
WHERE (birth_date LIKE '1900%')
ORDER BY birth_date DESC
LIMIT 3;

-- 7. Find the number of Nobel Prizes awarded between 1950 and 1960.

SELECT(COUNT(year))
FROM prize
WHERE (year >= 1950) and (year <= 1960);

-- 8. Find the number of Nobel Prizes awarded in each year.

SELECT year, COUNT(year) AS total_year
FROM prize
GROUP BY year;

-- 9. In which year was the greatest number of Nobel Prizes awarded?

SELECT year
FROM prize
GROUP BY year
ORDER BY COUNT(*) DESC
LIMIT 1;

-- 10. What is the average number of Nobel Prizes awarded per year? Do we know how to do this yet?

SELECT AVG(total_year)
FROM (SELECT year, COUNT(year) as total_year
	  FROM prize
	  GROUP BY year) AS T1;
	 
or;
	 
SELECT MAX(id) / (MAX(year) - MIN(year) + 1)
FROM prize;

no we don't;

-- 11. In which years were more than fifteen Nobel Prizes awarded?

SELECT year, COUNT(year) AS total_year
FROM prize
GROUP BY year
HAVING (COUNT(year) > 15);

-- 12. Who is the Nobel Laureate with the shortest name?

SELECT name, LENGTH(name) as name_length
FROM laureate
ORDER BY LENGTH(name) ASC;

-- 13. Which Nobel Laureate had the longest life? You might need to use IFNULL().

SELECT name, TIMESTAMPDIFF(year, birth_date, IFNULL(death_date, CURDATE())) AS age
FROM laureate
ORDER BY age DESC;

-- 14. Which year has the most women Nobel Laureates?


SELECT COUNT(sex) AS sex_count, sex, year
FROM laureate
JOIN prize
ON laureate.id = prize.laureate_id
WHERE (sex = 'F')
GROUP BY year, sex
ORDER BY sex_count DESC
LIMIT 1;


-- 15. Which category has the most women Nobel Laureates?

SELECT COUNT(sex) AS sex_count, sex, category
FROM laureate
JOIN prize
ON laureate.id = prize.laureate_id
WHERE (sex = 'F')
GROUP BY category, sex
ORDER BY sex_count DESC
LIMIT 1;



-- 16. What is the average number of Nobel Prizes awarded per year?
SELECT AVG(total_year)
FROM (SELECT year, COUNT(year) as total_year
	  FROM prize
	  GROUP BY year) AS T1;
