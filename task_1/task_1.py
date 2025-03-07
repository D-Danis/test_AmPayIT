# Задание 1: Python + SQL (базовое)
# Описание задачи:  

# Напишите скрипт на Python, который подключается 
# к базе данных (например, SQLite) и выполняет следующие действия:  
# 1. Создает таблицу `employees` с полями: `id`, `name`, `position`, `salary`.  
# 2. Добавляет в таблицу 5 тестовых записей.  
# 3. Выполняет запрос, который выводит всех сотрудников, у которых зарплата больше 50 000.  
# 4. Обновляет зарплату сотрудника с именем "Иван" до 60 000.  
# 5. Удаляет сотрудника с именем "Анна".  


import sqlite3


def create_connection(db_file):
    """Создать соединение с SQLite базой данных."""
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn):
    """Создает таблицу employees в базе данных."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL
        )
    ''')
    conn.commit()


def add_test_employees(conn):
    """Добавляет тестовые записи сотрудников в таблицу."""
    test_employees = [
        ("Иван", "Менеджер", 55000),
        ("Анна", "Разработчик", 48000),
        ("Петр", "Тестировщик", 52000),
        ("Светлана", "Дизайнер", 40000),
        ("Игорь", "Аналитик", 65000)
    ]
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)', test_employees)
    conn.commit()


def fetch_high_salary_employees(conn):
    """Возвращает сотрудников с зарплатой больше 50 000."""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE salary > 50000')
    return cursor.fetchall()


def update_employee_salary(conn, name, new_salary):
    """Обновляет зарплату сотрудника по имени."""
    cursor = conn.cursor()
    cursor.execute('UPDATE employees SET salary = ? WHERE name = ?', (new_salary, name))
    conn.commit()


def delete_employee_by_name(conn, name):
    """Удаляет сотрудника по имени."""
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE name = ?', (name,))
    conn.commit()

  
def main():
    """Главная функция для выполнения операций с базой данных."""
    database = "task_1/employees.db"

    # 1. Создает таблицу `employees` с полями: `id`, `name`, `position`, `salary`.  
    conn = create_connection(database)
    create_table(conn)
    
    # 2. Добавляет в таблицу 5 тестовых записей.
    add_test_employees(conn)

    # 3. Выполняет запрос, который выводит всех сотрудников, у которых зарплата больше 50 000. 
    print("Сотрудники с зарплатой больше 50 000:")
    high_salary_employees = fetch_high_salary_employees(conn)
    for employee in high_salary_employees:
        print(employee)
    
    # 4. Обновляет зарплату сотрудника с именем "Иван" до 60 000.
    update_employee_salary(conn, "Иван", 60000)
    
    # 5. Удаляет сотрудника с именем "Анна".
    delete_employee_by_name(conn, "Анна")

    conn.close()

if __name__ == "__main__":
    main()