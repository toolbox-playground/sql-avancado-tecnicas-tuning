import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker

fake = Faker()

# Quantidade de registros
NUM_CUSTOMERS = 10000
NUM_PRODUCTS = 2000
NUM_ORDERS = 50000
NUM_ORDER_ITEMS = 200000
NUM_MEDIA_CONTENT = 1000
NUM_STREAMING_HISTORY = 50000

# Funções auxiliares
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Gerar clientes
customers = [{
    "id": i + 1,
    "name": fake.name(),
    "email": fake.email(),
    "created_at": fake.date_time_between(start_date='-3y', end_date='now'),
    "status": random.choice(["active", "inactive", "banned"])
} for i in range(NUM_CUSTOMERS)]

# Gerar produtos
products = [{
    "id": i + 1,
    "name": fake.word().capitalize() + " " + fake.word().capitalize(),
    "category": random.choice(["Books", "Games", "Movies", "Electronics", "Clothing"]),
    "price": round(random.uniform(5, 500), 2),
    "available_stock": random.randint(0, 1000),
    "created_at": fake.date_time_between(start_date='-2y', end_date='now')
} for i in range(NUM_PRODUCTS)]

# Gerar mídia
media_content = [{
    "id": i + 1,
    "title": fake.sentence(nb_words=4),
    "type": random.choice(["movie", "series", "podcast"]),
    "genre": random.choice(["Action", "Drama", "Comedy", "Sci-Fi", "Horror"]),
    "release_date": fake.date_between(start_date='-10y', end_date='today'),
    "rating": round(random.uniform(1.0, 5.0), 1)
} for i in range(NUM_MEDIA_CONTENT)]

# Gerar pedidos
orders = [{
    "id": i + 1,
    "customer_id": random.randint(1, NUM_CUSTOMERS),
    "order_date": fake.date_time_between(start_date='-2y', end_date='now'),
    "total_amount": 0.0,  # a ser calculado depois
    "status": random.choice(["shipped", "processing", "cancelled", "returned"])
} for i in range(NUM_ORDERS)]

# Gerar itens do pedido
order_items = []
for i in range(NUM_ORDER_ITEMS):
    order_id = random.randint(1, NUM_ORDERS)
    product_id = random.randint(1, NUM_PRODUCTS)
    quantity = random.randint(1, 5)
    unit_price = round(random.uniform(10, 300), 2)
    order_items.append({
        "id": i + 1,
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "unit_price": unit_price
    })

# Gerar histórico de streaming
streaming_history = [{
    "id": i + 1,
    "customer_id": random.randint(1, NUM_CUSTOMERS),
    "media_id": random.randint(1, NUM_MEDIA_CONTENT),
    "watched_at": fake.date_time_between(start_date='-2y', end_date='now'),
    "duration_minutes": random.randint(10, 180)
} for i in range(NUM_STREAMING_HISTORY)]

# Converter para DataFrames
df_customers = pd.DataFrame(customers)
df_products = pd.DataFrame(products)
df_orders = pd.DataFrame(orders)
df_order_items = pd.DataFrame(order_items)
df_media_content = pd.DataFrame(media_content)
df_streaming_history = pd.DataFrame(streaming_history)

import ace_tools as tools; tools.display_dataframe_to_user(name="Clientes (customers)", dataframe=df_customers)
