SELECT * FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE LOWER(c.email) LIKE '%gmail.com%';

SELECT name, (
    SELECT COUNT(*) FROM orders o
    WHERE o.customer_id = c.id
) AS total_orders
FROM customers c
WHERE c.status = 'active';

SELECT * FROM products
WHERE category = 'Books'
   OR category = 'Games'
   OR category = 'Movies'
   OR category = 'Electronics';

SELECT * FROM products
WHERE category = 'Books'
   OR category = 'Games'
   OR category = 'Movies'
   OR category = 'Electronics';

SELECT * FROM media_content
WHERE EXTRACT(YEAR FROM release_date) = 2020;

SELECT * FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
JOIN customer_streaming_history sh ON c.id = sh.customer_id;
