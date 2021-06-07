/*
Write a query to find the month number (Eg: 4 corresponds to April) in which the most number of payments were made
*/

SELECT 
	month(payment_date) as Payment_month,
	COUNT(*) as No_of_payments
FROM payment
GROUP BY
	month(payment_date)
ORDER BY
	No_of_payments DESC
LIMIT 1;

/*
List the rounded average film lengths for each film category. Arrange the values in the decreasing order of the average film lengths.
*/

SELECT 
	ROUND(AVG(f.length),0) AS avg_Length,
	c.name AS name
FROM film as f
LEFT JOIN
	film_category as fc
	ON f.film_id = fc.film_id
    INNER JOIN
		category as c
        ON c.category_id=fc.category_id
GROUP BY
	c.name
ORDER BY
	avg_length DESC
;
/*
Write a query to find the number of occurrences of each film_category in each city. Arrange them in the decreasing order of their category count.
*/


SELECT 
cat.name AS name,
ci.city AS city,
COUNT(*) AS category_count
FROM payment as p
INNER JOIN 
	customer as c
    using(customer_id)
    INNER JOIN 
		address as a
        using(address_id)
        INNER JOIN
        city as ci
        using(city_id)
	INNER JOIN
		rental as r
        ON p.rental_id=r.rental_id
		INNER JOIN 
			inventory as i
            ON r.inventory_id=i.inventory_id
			INNER JOIN
				film as f
				ON i.film_id=f.film_id
                INNER JOIN
					film_category as fc
                    ON fc.film_id=f.film_id
                    INNER JOIN
						category as cat
                        ON fc.category_id=cat.category_id
GROUP BY
	cat.name, ci.city
ORDER BY 
	category_count DESC
;


/* 
upgrad way

18:21:15	SELECT   cat.name,   c.city  FROM inventory AS inv  INNER JOIN  store as st     ON inv.store_id=st.store_id     INNER JOIN   address as a         ON st.address_id=a.city_id     INNER JOIN             city as c             ON a.city_id=c.city_id INNER JOIN  film AS f     ON inv.film_id=f.film_id  INNER JOIN   film_category as fc         ON fc.film_id=f.film_id    INNER JOIN    category as cat             ON cat.category_id=fc.category_id GROUP BY  cat.name LIMIT 0, 1000	Error Code: 1055. Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'sakila.c.city' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by	0.00044 sec
SHOW TABLE
*************************** 1. row ***************************
address
*************************** 2. row ***************************
category
*************************** 3. row ***************************
city
*************************** 4. row ***************************
film_category
*************************** 5. row ***************************
inventory
*************************** 6. row ***************************
store
keyboard_arrow_up


 */
 
 SELECT
	cat.name AS name,
	ci.city AS city,
    count(*) AS category_count
 FROM inventory AS inv
 INNER JOIN
	store as st
    ON st.store_id=inv.store_id
    INNER JOIN
		address as a
        ON a.address_id=st.address_id
        INNER JOIN
        city as ci
        ON ci.city_id=a.city_id
INNER JOIN
	film AS f
    ON inv.film_id=f.film_id
	INNER JOIN
		film_category as fc
        ON fc.film_id=f.film_id
			INNER JOIN
			category as cat
            ON cat.category_id=fc.category_id
GROUP BY
	cat.name, ci.city
ORDER BY
	category_count DESC
 ;
 
 /*
 Suppose you are running an advertising campaign in Canada for which you need the film_ids and titles of all the films released in Canada.
 List the films in the alphabetical order of their titles.
 
 given tables
*************************** 1. row ***************************
address
*************************** 2. row ***************************
city
*************************** 3. row ***************************
country
*************************** 4. row ***************************
film
*************************** 5. row ***************************
inventory
*************************** 6. row ***************************
store

OUTPUT
	Film_id, Title
 */
 
 SELECT 
	DISTINCT f.film_id AS Film_id,
    f.title AS Title
 FROM
	film as f
    INNER JOIN
    inventory
    USING(film_id)
		INNER JOIN
		store
        USING(store_id)
			INNER JOIN
            address
            USING(address_id)
				INNER JOIN
					city
                    USING(city_id)
                    INNER JOIN
						country as c
                        USING(country_id)
WHERE c.country='Canada'
ORDER BY Title ASC
    ;
 /*
 Write a query to list all the films existing in the 'Comedy' category and arrange them in the alphabetical order.
 *************************** 1. row ***************************
category
*************************** 2. row ***************************
film
*************************** 3. row ***************************
film_category

OUTPUT 
title
 
 */
 
SELECT f.title
FROM film AS f
INNER JOIN
	film_category
    using(film_id)
    INNER JOIN
		category AS cat
		using(category_id)
WHERE
	cat.name="Comedy"
ORDER BY
	f.title ASC;
    
SELECT DISTINCT name
FROM category;
 
 
 /*
 List the first and last names of all customers whose first names start with the letters 'A', 'J' or 'T' or last names end with the substring 'on'. Arrange them alphabetically in the order of their first names.


 */

SELECT 
	first_name AS First_Name,
    last_name AS Last_name
FROM customer 
WHERE ((first_name LIKE 'A%') OR (first_name LIKE 'J%') OR (first_name LIKE 'T%')) OR (last_name LIKE '%on')
ORDER By first_name ;


select First_name, Last_name
from customer
where first_name regexp '^[ajt]' or last_name regexp 'on$'
order by first_name;
	