# Задание 7: Практическое (Python + SQL)  
# Описание задачи:  

# Напишите скрипт на Python, который:  

# 1. Подключается к базе данных (например, PostgreSQL).  
# 2. Создает таблицу `products` с полями: `id`, `name`, `price`, `quantity`.  
# 3. Добавляет 10 тестовых продуктов.  
# 4. Реализует функцию, которая возвращает список продуктов, у которых количество меньше 10.  
# 5. Реализует функцию, которая обновляет цену продукта по его имени.  

import psycopg2
from psycopg2 import sql

def create_connection():
    """Подключение к базе данных PostgreSQL"""
    try:
        conn = psycopg2.connect(
            dbname='your_dbname',      # Укажите свое имя базы данных
            user='your_username',      # Укажите пользователя
            password='your_password',  # Укажите пароль
            host='localhost',          
            port='5432'                
        )
        return conn
    except Exception as e:
        print(f"Ошибка подключения к БД: {e}")

def create_table(conn):
    """Создание таблицы products"""
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                quantity INT NOT NULL
            )
        """)
        conn.commit()

def add_test_products(conn):
    """Добавление 10 тестовых продуктов"""
    products = [
        ('Product 1', 10.99, 5),
        ('Product 2', 20.50, 15),
        ('Product 3', 5.50, 2),
        ('Product 4', 30.00, 10),
        ('Product 5', 25.00, 0),
        ('Product 6', 15.75, 8),
        ('Product 7', 40.50, 4),
        ('Product 8', 12.00, 12),
        ('Product 9', 22.10, 3),
        ('Product 10', 7.30, 14)
    ]

    with conn.cursor() as cursor:
        cursor.executemany("""
            INSERT INTO products (name, price, quantity)
            VALUES (%s, %s, %s)
        """, products)
        conn.commit()

def get_low_stock_products(conn):
    """Возвращает список продуктов, у которых количество меньше 10"""
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM products WHERE quantity < 10")
        return cursor.fetchall()

def update_product_price(conn, product_name, new_price):
    """Обновляет цену продукта по его имени"""
    with conn.cursor() as cursor:
        cursor.execute("""
            UPDATE products
            SET price = %s
            WHERE name = %s
        """, (new_price, product_name))
        conn.commit()


# Основная логика
def main():
    # 1. Подключается к базе данных (например, PostgreSQL).  
    conn = create_connection()

    if conn:
        # 2. Создает таблицу `products` с полями: `id`, `name`, `price`, `quantity`.  
        create_table(conn)
        
        # 3. Добавляет 10 тестовых продуктов.
        add_test_products(conn)
        
        # 4. Функцию, которая возвращает список продуктов, у которых количество меньше 10.
        print("Продукты с количеством менее 10:")
        low_stock_products = get_low_stock_products(conn)
        for product in low_stock_products:
            print(product)

        # 5. Обновление цены для примера
        product_name_to_update = 'Product 1'
        new_price = 12.99
        update_product_price(conn, product_name_to_update, new_price)
        
        print(f"\nОбновлена цена для {product_name_to_update}: {new_price}")

        conn.close()
        
        
if __name__ == "__main__":
    main()