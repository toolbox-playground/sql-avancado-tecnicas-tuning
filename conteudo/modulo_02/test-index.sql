EXPLAIN SELECT *
FROM employees
WHERE firstName = 'Maria';

------------------------------

EXPLAIN SELECT *
FROM employees
WHERE firstName = 'Maria' AND lastName = 'Alves';

------------------------------

EXPLAIN SELECT *
FROM employees
WHERE lastName = 'Alves';