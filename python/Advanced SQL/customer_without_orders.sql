/*
Problem statement: Extract the required details of the customers who have not placed an order yet
Expected columns: The columns that are required as the output are as follows:

'cust_id'
'cust_name'
'city'
'state'
'customer_segment'
A flag to indicate that there is another customer with the exact same name and city but a different customer ID.

The tables that are required for solving this problem are as follows:

'cust_dimen'
'market_fact_full'

*/

-- Exploring customer dimension table
SELECT 
	* 
FROM cust_dimen;

-- List all the customers who have not placed any order
SELECT c.*
FROM
	cust_dimen AS c
LEFT JOIN
	market_fact_full AS m
    ON c.cust_id=m.cust_id
WHERE m.ord_id IS NULL;

-- checking if really no such customers exist
SELECT COUNT(cust_id) FROM cust_dimen;
-- 1832
SELECT COUNT(DISTINCT cust_id) FROM market_fact_full;
-- 1832

-- List all the customers who have placed order once
SELECT c.*,
	COUNT(DISTINCT ord_id) AS order_count
FROM
	cust_dimen AS c
LEFT JOIN
	market_fact_full AS m
    ON c.cust_id=m.cust_id
GROUP BY cust_id
HAVING COUNT(DISTINCT ord_id)<>1;
;
-- Unique Customer name and city check
SELECT customer_name,
	city,
    COUNT(cust_id) AS cust_id_count
FROM cust_dimen
GROUP BY
	Customer_Name,
    city
HAVING COUNT(cust_id) >1;

-- Final output

WITH cust_details AS
(
SELECT c.*,
	COUNT(DISTINCT ord_id) AS order_count
FROM cust_dimen AS c
LEFT JOIN 
	market_fact_full AS m
    ON c.cust_id=m.cust_id
GROUP BY
	cust_id
HAVING COUNT(DISTINCT ord_id) <>1
),
fraud_cust_list AS (

SELECT customer_name,
	city,
    COUNT(cust_id) AS cust_id_count
FROM cust_dimen
GROUP BY
	Customer_Name,
    city
HAVING COUNT(cust_id) >1
)
SELECT cd.*,
	CASE WHEN fc.cust_id_count IS NOT NULL 
		THEN 'FRAUD'
	ELSE 'NORMAL'
	END AS fraud_flag
FROM 
	cust_details as cd
    LEFT JOIN 
    fraud_cust_list as fc
		ON cd.customer_name=fc.customer_name AND
			cd.city=fc.city
;