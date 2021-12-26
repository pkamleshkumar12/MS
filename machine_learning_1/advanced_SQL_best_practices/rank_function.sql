-- RANK function
/*
RANK() over (
 	PARTITION BY <expression>[{, <expression>...}]
    ORDER BY <expression> [ASC|DESC],[{, <expression>...}]
)
*/
USE market_star_schema;

SELECT customer_name,
	ord_id,
	round(sales) AS rounded_sales,
    RANK() OVER(ORDER BY sales DESC) AS sales_rank
FROM market_fact_full as m
INNER JOIN
cust_dimen as c
ON m.cust_id = c.cust_id
WHERE customer_name = 'RICK WILSON';

-- RANK Top 10 sales orders from a customer
WITH rank_info AS (
SELECT customer_name,
	ord_id,
	round(sales) AS rounded_sales,
    RANK() OVER(ORDER BY sales DESC) AS sales_rank
FROM market_fact_full as m
INNER JOIN
cust_dimen as c
ON m.cust_id = c.cust_id
WHERE customer_name = 'RICK WILSON'
)
SELECT * 
FROM rank_info
WHERE sales_rank <=10;

-- Analytical function: DENSE_RANK() and PERCENT_RANK()

/*
DENSE_RANK() over (
 	PARTITION BY <expression>[{, <expression>...}]
    ORDER BY <expression> [ASC|DESC],[{, <expression>...}]
)
PERCENT_RAN() over (
 	PARTITION BY <expression>[{, <expression>...}]
    ORDER BY <expression> [ASC|DESC],[{, <expression>...}]
)
*/

-- Example for DENSE RANK
SELECT 
	ord_id,
    discount,
    customer_name,
    RANK() OVER(ORDER BY discount DESC) as disc_rank,
    DENSE_RANK() OVER(ORDER BY discount DESC) as disc_dense_rank
FROM market_fact_full as m
INNER JOIN cust_dimen as c
ON m.cust_id=c.cust_id
WHERE customer_name='GIULIETTA BAPTIST';
	
/*
you can use the 'row number' function for the following use cases:
To determine the top 10 selling products out of a large variety of products
To determine the top three winners in a car race
To find the top five areas in different cities in terms of GDP growth
*/

/* 
ROW_NUMBER SYNTAX

ROW_NUMBER() OVER (
		PARTION BY <expression>[{, <expression>...}]
        ORDER BY <expression> [ASC|DESC],[{, <expression>...}]
)
*/
-- Number of orders each customers has placed

SELECT customer_name,
	COUNT(DISTINCT ord_id) as order_count, 
    RANK() OVER(ORDER BY COUNT(DISTINCT ord_id) DESC) as order_rank,
    DENSE_RANK() OVER(ORDER BY COUNT(DISTINCT ord_id) DESC) as order_dense_rank,
    ROW_NUMBER() OVER(ORDER BY COUNT(DISTINCT ord_id) DESC) as order_row_num
FROM market_fact_full AS m
INNER JOIN
cust_dimen AS c
ON m.cust_id=c.cust_id
GROUP BY customer_name;

-- Partitioning example, by ship_mode
WITH shipping_summary AS
(SELECT ship_mode,
	month(ship_date) as shipping_month,
    COUNT(*) as shipments
FROM
	shipping_dimen
    GROUP BY ship_mode, 
			month(ship_date)
)
SELECT *,
	RANK() OVER( PARTITION BY ship_mode ORDER BY shipments DESC) AS shipping_month
FROM shipping_summary;

/*
Named Windows
WINDOW window_name AS (window_spec)
  [, window_name AS (window_spec)] ...


The order in which the various SQL statements appear in a query is as follows: 

SELECT
FROM
JOIN
WHERE
GROUP BY
HAVING
WINDOW
ORDER BY
*/

SELECT ord_id,
	discount,
    customer_name,
    RANK() OVER w AS disc_rank,
    DENSE_RANK() OVER w AS disc_dense_rank,
    ROW_NUMBER() OVER w AS disc_row_num
FROM market_fact_full as m
INNER JOIN cust_dimen as c
ON m.cust_id=c.cust_id
-- WHERE customer_name = 'RICK WILSON'
WINDOW w AS (PARTITION BY customer_name ORDER BY discount DESC);

/* rewrite the following query */
SELECT *,
RANK() OVER (
  PARTITION BY ship_mode
  ORDER BY COUNT(*)) 'Rank',
DENSE_RANK() OVER (
  PARTITION BY ship_mode
  ORDER BY COUNT(*)) 'Dense Rank',
PERCENT_RANK() OVER (
  PARTITION BY ship_mode
  ORDER BY COUNT(*)) 'Percent Rank'
FROM shipping_dimen;

/*
solution
*/
SELECT *,
RANK() OVER w AS 'Rank',
DENSE_RANK() OVER w AS 'Dense Rank',
PERCENT_RANK() OVER w AS 'Percent Rank'
FROM shipping_dimen
WINDOW w AS( PARTITION BY ship_mode ORDER BY COUNT(*)  DESC);
/* solution from upgrad site */

SELECT *,
RANK() OVER w 'Rank',
DENSE_RANK() OVER w 'Dense Rank',
PERCENT_RANK() OVER w 'Percent Rank'
FROM shipping_dimen
WINDOW w AS (
  PARTITION BY ship_mode
  ORDER BY COUNT(*)
);

/*
Frames example

*/
WITH daily_shipping_summary AS 
(
SELECT ship_date, 
	SUM(shipping_cost) AS daily_total
FROM
market_fact_full as m
INNER JOIN
shipping_dimen as s
ON m.ship_id = s.ship_id
GROUP BY ship_date
)
SELECT *,
	SUM(daily_total) OVER w1 AS running_total,
    AVG(daily_total) OVER w2 AS moving_avg
FROM daily_shipping_summary
WINDOW w1 as (ORDER BY daily_total ROWS UNBOUNDED PRECEDING), w2 as (ORDER BY daily_total ROWS 6 PRECEDING);

/*

select * 
    avg(runs) OVER (ORDER BY `year` ROWS BETWEEN 4 PRECEDING AND CURRENT ROW)
    as "Moving Average"
from Kohli_Batting
*/

/*
Lead and Lag Functions syntax

LEAD(expr[, offset[, default]])
  OVER (Window_specification | Window_name) 

LAG(expr[, offset[, default]])
  OVER (Window_specification | Window_name)
 
  use case of the 'lead' and 'lag' functions is to determine whether consecutive orders were shipped using the same shipping mode
*/

-- Lead and Lag Example
WITH cust_order as 
(
SELECT c.customer_name,
	m.ord_id,
    o.order_date
FROM 
market_fact_full as m
LEFT JOIN
orders_dimen as o
ON m.ord_id=o.ord_id
LEFT JOIN
cust_dimen as c
ON m.cust_id=c.cust_id
WHERE customer_name='RICK WILSON'
GROUP BY
	c.customer_name,
    m.ord_id,
    o.order_date
),
next_date_summary AS 
(SELECT *,
	LEAD(order_date, 1, '2015-01-01') OVER (ORDER BY order_date, ord_id) AS next_order_date
FROM cust_order
ORDER BY customer_name,
	order_date,
    ord_id
)
SELECT *, DATEDIFF(next_order_date, order_date) as days_diff
FROM next_date_summary;
/*
CASE WHEN Statements


CASE
  WHEN condition1 THEN result1
  WHEN condition2 THEN result2
  .
  .
  WHEN conditionN THEN resultN
  ELSE result
END AS column_name;

*/

/*
Example: CASE WHEN
profit < -500 => Huge lose
profit -500 to 0 => Bearable lose
profit 0 to 500 => Decent profit
profit > 500 => Great profit
*/

SELECT 
	market_fact_id,
    profit,
    CASE
		WHEN profit < -500 THEN 'Huge Loss'
        WHEN profit BETWEEN -500 AND 0 THEN 'Bearable loss'
        WHEN profit BETWEEN 0 AND 500 THEN 'Decent Profit'
		ELSE 'Great Profit'
	END AS Profit_type
    
FROM
	market_fact_full;
    
/*
Classify customers on the following criteria
Top 10% of customer as Gold
Next 40% of customers as Silver
Rest 50% of customers as Bronze
*/
WITH cust_summary AS  
(
	SELECT 
		m.cust_id, 
		c.customer_name, 
		ROUND(SUM(m.sales)) as total_sales,
		PERCENT_RANK() OVER(ORDER BY SUM(m.sales) DESC) as perc_rank
	FROM
		market_fact_full as m
		LEFT JOIN
		cust_dimen as c
	ON
		m.cust_id=c.cust_id
	GROUP BY cust_id
)
SELECT *,
	CASE 
		WHEN perc_rank < 0.1 THEN 'Gold'
        WHEN perc_rank < 0.5 THEN 'Silver'
        ELSE 'Bronze'
	END AS customer_category
FROM cust_summary;

/*
CREATE FUNCTION is a DDL Statment
Syntax:
DELIMITER $$

CREATE FUNCTION function_name(func_parameter1, func_parameter2, ...)
  RETURN datatype [characteristics]
  BEGIN
    <SQL Statements>
    RETURN expression;
END $$

DELIMITER ;

CALL function_name;
*/