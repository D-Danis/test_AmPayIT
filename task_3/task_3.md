# Задание 3: SQL (запросы)  
# Описание задачи:  

# Дана таблица `orders` с полями:  
- `id` (уникальный идентификатор заказа),  
- `customer_id` (идентификатор клиента),  
- `order_date` (дата заказа),  
- `amount` (сумма заказа).  

# Напишите SQL-запросы для следующих задач:  
1. Найти общую сумму заказов для каждого клиента.  
2. Найти клиента с максимальной суммой заказов.  
3. Найти количество заказов, сделанных в 2023 году.  
4. Найти среднюю сумму заказа для каждого клиента.

# 1. Найти общую сумму заказов для каждого клиента. 
```SQL
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id;
```


# 2. Найти клиента с максимальной суммой заказов.
```SQL
SELECT customer_id, SUM(amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 1;
```


# 3. Найти количество заказов, сделанных в 2023 году.  
```sql
SELECT COUNT(*) AS total_orders
FROM orders
WHERE YEAR(order_date) = 2023;
```

# 4. Найти среднюю сумму заказа для каждого клиента.   
```sql
SELECT customer_id, AVG(amount) AS average_order_amount
FROM orders
GROUP BY customer_id;
```
