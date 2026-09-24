-- Write your query below
SELECT name FROM customers WHERE id NOT IN (select customer_id from orders)