/*
Stored Procedure Syntax

DELIMITER $$

CREATE PROCEDURE Procedure_name (<Paramter List>)
BEGIN
  <SQL Statements>
END $$

DELIMITER ;

CALL Procedure_name;
*/

DELIMITER $$
CREATE PROCEDURE get_sales_customers (sales_input INT)
BEGIN	
	SELECT cust_id,
					ROUND(sales) as sales_amount
	FROM
		market_fact_full
	WHERE ROUND(sales) > sales_input
	ORDER BY sales;

END $$
DELIMITER ;

CALL get_sales_customers(300);

DROP PROCEDURE get_sales_customers;





 -- 19:15:50	CALL get_sales_customers(300)	Error Code: 3065. Expression #1 of ORDER BY clause is not in SELECT list, references column 'market_star_schema.market_fact_full.Sales' which is not in SELECT list; this is incompatible with DISTINCT	0.00053 sec







