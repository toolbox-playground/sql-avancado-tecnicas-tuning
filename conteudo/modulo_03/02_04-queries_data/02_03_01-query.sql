SELECT *
FROM customers c
JOIN orders o ON o.customerNumber = c.customerNumber
WHERE c.country = 'Country60'

-- Exemplo de Expain

EXPLAIN SELECT *
FROM customers c
JOIN orders o ON o.customerNumber = c.customerNumber
WHERE c.country = 'Country60'

-- Exemplo de Tuning

SELECT *
FROM orders as o
JOIN (select * from customers where country = 'Country60' ) as c
ON o.customerNumber = c.customerNumber
