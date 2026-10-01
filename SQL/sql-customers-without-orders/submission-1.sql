-- Write your query below
SELECT name FROM customers WHERE Id NOT IN (SELECT customer_id FROM orders)