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

DELIMITER $$
CREATE FUNCTION profitType(profit int) 
RETURNS VARCHAR(30) DETERMINISTIC

BEGIN

DECLARE message VARCHAR(30);
IF profit< -500 THEN
	SET message = 'Huge Loss';
ELSEIF profit BETWEEN -500 AND 0 THEN
	SET message = 'Bearable Loss';
ELSEIF profit BETWEEN 0 AND 500 THEN
	SET message = 'Decent Profit';
ELSE
	SET message='Great profit';
END IF;

RETURN message;

END;
$$
DELIMITER ;

SELECT profitType(-600) AS Function_output;
