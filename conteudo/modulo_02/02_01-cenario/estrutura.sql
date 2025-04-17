-- Tabela de Clientes
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    created_at TIMESTAMP,
    status VARCHAR(50)
);

-- Tabela de Produtos
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10,2),
    available_stock INT,
    created_at TIMESTAMP
);

-- Tabela de Pedidos
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date TIMESTAMP,
    total_amount DECIMAL(10,2),
    status VARCHAR(50)
);

-- Itens do pedido
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT,
    unit_price DECIMAL(10,2)
);

-- Streaming: Filmes e Séries
CREATE TABLE media_content (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    type VARCHAR(50), -- movie, series, podcast
    genre VARCHAR(100),
    release_date DATE,
    rating DECIMAL(3,2)
);

-- Histórico de consumo do cliente (streaming)
CREATE TABLE customer_streaming_history (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    media_id INT REFERENCES media_content(id),
    watched_at TIMESTAMP,
    duration_minutes INT
);
