/*
Problem statement: Get the details of TOP 10 profitable customers in form of a table shown below:

cust_id
rank
customer_name
profit
customer_city
customer_state
sales
*/
-- Exploring cus_dimen table

SELECT 
	cust_id,
    customer_name,
    city as customer_city,
    state as customer_state
FROM
	cust_dimen
WHERE cust_id like 'cust_1%'
;
-- Ranking

WITH cust_summary AS
(
	SELECT 
		c.cust_id,
        RANK() OVER(ORDER BY SUM(profit) DESC) as customer_rank,
		customer_name,
        ROUND(SUM(profit), 2) as profit,
		city as customer_city,
		state as customer_state,
        ROUND(SUM(sales), 2) as sales
	FROM
		cust_dimen AS c
        INNER JOIN 
			market_fact_full as m
			ON c.cust_id=m.cust_id
	GROUP BY 
		c.cust_id
)
SELECT * FROM cust_summary
WHERE customer_rank <=10
;

