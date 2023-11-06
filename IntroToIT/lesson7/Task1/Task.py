#INTRO TO IT 2nd COURSE

#Функция производит сложение двух чисел
def add_numbers(a, b):
    """Функция принимает только два числа и возвращает их сумму"""
    result = a + b
    return result

#Функция производит умножение двух чисел
def multiply_numbers(a, b):
    """Функция принимает только два числа и возвращает их произведение"""
    result = a * b
    return result

#Функция находит максимальное значение числа из списка
def find_max_number(numbers):
    """Функция принимает любое количество чисел списка и возвращает максимальное значение"""
    max_number = max(numbers)
    return max_number

#Функция находит факториал числа
def calculate_factorial(n):
    """Функция принимает только одно число и возвращает его факториал"""
    if n == 0:
        return 1
    factorial = 1
    """С помощью range функция прохидится по всем значениям, нужным для вычесления факторияла числа"""
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#Функция выясняет четность значения числа
def is_even(number):
    """Функция принимает только одно число и, узнав остаток числа после деления на 2
    возвращает ответ о чётности числа"""
    if number % 2 == 0:
        return True
    else:
        return False

num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
numbers_list = [3, 8, 1, 6, 12]
max_num = find_max_number(numbers_list)
num4 = 5
factorial_result = calculate_factorial(num4)
num3 = 7
is_even_num = is_even(num3)

print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа {num4} равен {factorial_result}")
if is_even_num == True:
    print(f"Число {num3} - четное.")
else:
    print(f"Число {num3} - нечетное.")