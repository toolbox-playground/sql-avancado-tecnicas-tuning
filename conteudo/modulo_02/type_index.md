Vamos usar exemplos práticos para cada tipo de índice no MySQL.

-----

### B-Tree (Padrão)

Este é o tipo de índice mais comum. Se você não especificar o tipo de índice, o MySQL usará o B-Tree por padrão.

#### Exemplo

Suponha que você tenha a tabela `products` e queira acelerar consultas que buscam por um produto pelo seu código ou por uma faixa de preços.

```sql
-- Cria a tabela de exemplo
CREATE TABLE products (
    productCode VARCHAR(15) PRIMARY KEY,
    productName VARCHAR(70) NOT NULL,
    productLine VARCHAR(50) NOT NULL,
    buyPrice DECIMAL(10, 2) NOT NULL
);

-- Cria um índice B-Tree na coluna 'buyPrice' para buscas de preço
CREATE INDEX idx_buyPrice ON products (buyPrice);
```

#### Como Usar

Para testar, use a cláusula `EXPLAIN` em uma consulta que filtra por preço. Você verá que o MySQL usa o índice `idx_buyPrice` para otimizar a busca.

```sql
EXPLAIN SELECT *
FROM products
WHERE buyPrice > 50.00;
```

-----

### Full-Text

Este tipo de índice é ideal para buscas em colunas com muito texto.

#### Exemplo

Vamos criar um índice **Full-Text** na coluna `productDescription` de uma tabela `articles`.

```sql
-- Cria a tabela de exemplo com a coluna de texto
CREATE TABLE articles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL
);

-- Adiciona o índice Full-Text na coluna 'body'
CREATE FULLTEXT INDEX idx_body ON articles (body);
```

#### Como Usar

Você usa a sintaxe `MATCH ... AGAINST` para realizar a pesquisa.

```sql
-- Pesquisa por artigos que contenham a palavra 'database'
SELECT *
FROM articles
WHERE MATCH(body) AGAINST('database');
```

-----

### R-Tree

Usado para dados espaciais (latitude, longitude). O tipo de dado `SPATIAL` é fundamental para este índice.

#### Exemplo

Imagine que você tenha uma tabela `locations` com as coordenadas de pontos de interesse.

```sql
-- Cria a tabela com o tipo de dado 'POINT'
CREATE TABLE locations (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    coordinates POINT NOT NULL,
    SPATIAL INDEX(coordinates)
);
```

#### Como Usar

Você pode usar funções geográficas como `ST_Distance_Sphere` para encontrar pontos dentro de uma certa distância.

```sql
-- Busca por locais dentro de um raio de 1000 metros de um ponto específico
SELECT
    id,
    name
FROM locations
WHERE
    ST_Distance_Sphere(coordinates, POINT(-46.633308, -23.55052)) <= 1000;
```