# Задание 5: Алгоритмическое (Python)  
# Описание задачи:  

# Напишите функцию на Python, которая принимает на вход список чисел и возвращает:  
# 1. Количество уникальных чисел.  
# 2. Второе по величине число в списке.  
# 3. Список чисел, которые делятся на 3 без остатка.  
# Пример:  
# python  
# input_list = [10, 20, 30, 40, 50, 30, 20]  
# Ожидаемый результат:  
# Уникальные числа: 5  
# Второе по величине число: 40  
# Числа, делящиеся на 3: [30, 30]  


def analyze_numbers(input_list):
    # 1. Количество уникальных чисел
    unique_numbers = set(input_list)
    unique_count = len(unique_numbers)
    
    # 2. Второе по величине число
    sorted_unique_numbers = sorted(unique_numbers, reverse=True)
    second_largest = sorted_unique_numbers[1] if len(sorted_unique_numbers) > 1 else None
    
    # 3. Список чисел, которые делятся на 3 без остатка
    divisible_by_three = [num for num in input_list if num % 3 == 0]
    
    return unique_count, second_largest, divisible_by_three

# Пример использования
input_list = [10, 20, 30, 40, 50, 30, 20]
unique_count, second_largest, divisible_by_three = analyze_numbers(input_list)

# Ожидаемый результат:
print(f"Уникальные числа: {unique_count}")
print(f"Второе по величине число: {second_largest}")
print(f"Числа, делящиеся на 3: {divisible_by_three}")