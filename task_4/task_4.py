# Задание 4: Python (мини-проект)  
# Описание задачи:  

# Напишите небольшой скрипт на Python, который:  
# 1. Читает CSV-файл с данными о сотрудниках (например, `name, position, salary`).  
# 2. Записывает данные в базу данных (SQLite или PostgreSQL).  
# 3. Реализует функцию поиска сотрудников по должности (например, все разработчики).  
# 4. Реализует функцию обновления зарплаты сотрудника по его имени.  


import sqlite3
import pandas as pd


def read_csv(file_path):
    """Чтение CSV-файла"""
    return pd.read_csv(file_path)


def create_database(db_name):
    """Создание базы данных"""
    conn = sqlite3.connect(db_name)
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
    return conn


def insert_employees(conn, employees):
    """Запись данных в базу данных"""
    for _, employee in employees.iterrows():
        conn.execute('''
            INSERT INTO employees (name, position, salary)
            VALUES (?, ?, ?)
        ''', (employee['name'], employee['position'], employee['salary']))
    conn.commit()


def find_employees_by_position(conn, position):
    """Поиск сотрудников по должности"""
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees WHERE position = ?', (position,))
    return cursor.fetchall()


def update_salary(conn, name, new_salary):
    """Обновление зарплаты сотрудника по его имени"""
    cursor = conn.cursor()
    cursor.execute('UPDATE employees SET salary = ? WHERE name = ?', (new_salary, name))
    conn.commit()


# Основная логика выполнения
def main():
    csv_file_path = 'task_4/employees.csv'
    db_name = 'task_4/employees.db'

    # 1. Чтение CSV
    employees = read_csv(csv_file_path)

    # 2. Создание базы данных и запись данных
    conn = create_database(db_name)
    insert_employees(conn, employees)

    # 3. Пример поиска сотрудников
    position_to_search = 'developer'
    developers = find_employees_by_position(conn, position_to_search)
    print(f"Сотрудники на должности '{position_to_search}': {developers}")

    # 4. Пример обновления зарплаты
    employee_name = 'Alice'
    new_salary = 95000
    update_salary(conn, employee_name, new_salary)
    print(f"Обновленная зарплата для {employee_name} на {new_salary}")

    conn.close()

if __name__ == '__main__':
    main()