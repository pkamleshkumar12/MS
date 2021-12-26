/*
The command for creating an index is as follows:
CREATE INDEX index_name
ON table_name (column_1, column_2, ...);

The command for adding an index is as follows:
ALTER TABLE table_name
ADD INDEX index_name(column_1, column_2, ...);

The command for dropping an index is as follows:
ALTER TABLE table_name
DROP INDEX index_name;

*/

CREATE TABLE market_fact_temp AS
SELECT * 
FROM
	market_fact_full;
    
CREATE INDEX filter_index ON market_fact_temp(cust_id, ship_id, prod_id);

ALTER TABLE market_fact_temp DROP INDEX filter_index;