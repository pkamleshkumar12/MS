/*
Problem statement: Identify the sustainable (profitable) product categories so that the growth team can capitalise on them to increase sales.
Metrics: Some of the metrics that can be used for performing the profitability analysis are as follows:

Profits per product category
Profits per product subcategory
Average profit per order
Average profit percentage per order

	We can look at the profites per product category
    we can look at profits per product subcategory
    we can check Average profit per order
    Also, consider average profit % per order
	
*/

SELECT 
	p.Product_category,
    p.Product_Sub_Category,
    SUM(m.Profit) AS Profits
FROM
	market_fact_full as m
INNER JOIN 
	prod_dimen as p
ON m.prod_id=p.prod_id
GROUP BY
	p.Product_Category,
    p.Product_Sub_Category
ORDER BY p.Product_Category, 
		SUM(m.Profit)
;

-- Exploring order table

SELECT ord_id,
	order_number
FROM
	orders_dimen
GROUP BY
	ord_id,
    Order_Number
ORDER BY
	ord_id,
    order_number;

SELECT 
	COUNT(*) as rec_count,
    COUNT(DISTINCT ord_id) as ord_id_count,
    COUNT(DISTINCT order_number) as ord_number_count
FROM
	orders_dimen;

-- Average profit per order
SELECT 
	p.Product_category,
    SUM(m.Profit) AS Profits,
    ROUND(SUM(m.Profit) / COUNT(DISTINCT o.order_number), 2) as Avg_profit_per_order
FROM
	market_fact_full as m
INNER JOIN 
	prod_dimen as p
	ON m.prod_id=p.prod_id
		INNER JOIN 
			orders_dimen as o
			ON m.ord_id=o.ord_id
GROUP BY
	p.Product_Category
ORDER BY p.Product_Category, 
		SUM(m.Profit)
;
-- average profit % per order
SELECT 
	p.Product_category,
    SUM(m.Profit) AS Profits,
    COUNT(DISTINCT o.order_number) AS Total_orders,
    ROUND(SUM(m.Profit) / COUNT(DISTINCT o.order_number), 2) as Avg_profit_per_order,
	ROUND(SUM(m.Sales) / COUNT(DISTINCT o.order_number), 2) as Avg_sales_per_order,
    ROUND(SUM(m.Profit) / SUM(m.Sales), 4)*100 as Profit_perc
FROM
	market_fact_full as m
INNER JOIN 
	prod_dimen as p
	ON m.prod_id=p.prod_id
		INNER JOIN 
			orders_dimen as o
			ON m.ord_id=o.ord_id
GROUP BY
	p.Product_Category
ORDER BY p.Product_Category, 
		SUM(m.Profit)