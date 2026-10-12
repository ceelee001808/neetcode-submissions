-- Write your query below
SELECT sp.name
FROM sales_person sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM orders o
    JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON'
);

-- output: only the salesperson's name column
-- look at the sales_person table, nicknamed "sp"
-- keep a salesperson only if their ID is NOT in the list built below
-- the list: sales IDs taken from orders...
-- ...start from the orders table, nicknamed "o"
-- attach company info to each order, nicknamed "c"
-- match each order to its company by company ID
-- keep only orders placed with the company CRIMSON
-- end of list = everyone who ever sold to CRIMSON
-- final result = every salesperson NOT on that list