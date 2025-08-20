SELECT
  TABLE_NAME AS 'orders2',
  ROUND(((data_length + index_length) / 1024 / 1024), 2) AS 'Size (MB)'
FROM
  information_schema.TABLES
WHERE
  table_schema = 'treinamento'
  AND TABLE_NAME = 'orders2';

  ----------------

SHOW TABLE STATUS LIKE 'orders2';