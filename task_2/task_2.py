# Задание 2: Python (работа с данными)  
# Описание задачи:  
# Напишите функцию на Python, которая принимает на вход список словарей, 
# где каждый словарь представляет собой информацию о сотруднике:  
# python  
# employees = [  
#     {"name": "Иван", "position": "разработчик", "salary": 55000},  
#     {"name": "Анна", "position": "аналитик", "salary": 48000},  
#     {"name": "Петр", "position": "тестировщик", "salary": 52000},  
# ]  

# Функция должна:  
# 1. Вернуть список имен сотрудников, у которых зарплата больше 50 000.  
# 2. Вернуть среднюю зарплату всех сотрудников.  
# 3. Отсортировать сотрудников по зарплате в порядке убывания.  


def process_employee_data(employees):
    # 1. Список имен сотрудников с зарплатой больше 50 000
    high_salary_names = [employee['name'] for employee in employees if employee['salary'] > 50000]
    
    # 2. Средняя зарплата всех сотрудников
    total_salary = sum(employee['salary'] for employee in employees)
    average_salary = total_salary / len(employees) if employees else 0  # Убедитесь, что список не пустой

    # 3. Сортировка сотрудников по зарплате в порядке убывания
    sorted_employees = sorted(employees, key=lambda x: x['salary'], reverse=True)

    return high_salary_names, average_salary, sorted_employees

# Пример использования функции
employees = [
    {"name": "Иван", "position": "разработчик", "salary": 55000},
    {"name": "Анна", "position": "аналитик", "salary": 48000},
    {"name": "Петр", "position": "тестировщик", "salary": 52000},
]

high_salary_names, average_salary, sorted_employees = process_employee_data(employees)

print("Сотрудники с зарплатой выше 50 000:", high_salary_names)
print("Средняя зарплата:", average_salary)
print("Сотрудники, отсортированные по зарплате (убывание):", sorted_employees)