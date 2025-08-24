SELECT e.firstName, e.lastName, o.city
FROM employees e
LEFT JOIN offices o ON e.officeCode = o.officeCode
WHERE o.city = 'City7' OR o.country = 'Country7' OR o.postalCode = '1501';


---- Otimizada 

SELECT e.firstName, e.lastName, officeCode
FROM employees e
WHERE EXISTS (
  SELECT 1
  FROM offices
  WHERE
    e.officeCode = officeCode
    AND (
            city = 'City7' OR country = 'Country7' OR postalCode = '1501'    )
);

SELECT e.firstName, e.lastName, (select city from offices where e.officeCode = officeCode)
FROM employees e
WHERE EXISTS (
  SELECT 1
  FROM offices
  WHERE
    e.officeCode = officeCode
    AND (
            city = 'City7' OR country = 'Country7' OR postalCode = '1501'    )
);