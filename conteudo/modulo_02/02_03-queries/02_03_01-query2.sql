SELECT c.customerName, o.orderNumber
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
WHERE c.customerNumber IN (SELECT customerNumber FROM customers WHERE creditLimit > 1500);