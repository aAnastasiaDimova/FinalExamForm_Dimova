#INTRO TO IT 2nd COURSE
def add_numbers(a, b):
# Функция принимает 2 числа - a, b и возвращает их сумму
    result = a + b
    return result

def multiply_numbers(a, b):
# Функция принимает 2 числа - a, b и возвращает их произведение
    result = a * b
    return result

def find_max_number(numbers):
# Функция принимает числа - numbers и возвращает максимальное
    max_number = max(numbers)
    return max_number

def calculate_factorial(n):
 # Функция принимает число - n и возвращает его факториал
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def is_even(number):
# Функция принимает число - number. Возвращает True если
# число четное, False если нет
    if number % 2 == 0:
        return True
    else:
        return False

num1 = 10
num2 = 5
# Переменные для функций
sum_result = add_numbers(num1, num2)
# В sum_result записываем результат функции add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
# В product_result записываем результат функции multiply_numbers(num1, num2)
numbers_list = [3, 8, 1, 6, 12]
# Переменная со списком для функции
max_num = find_max_number(numbers_list)
# В max_num записываем результат функции find_max_number(numbers_list)
factorial_result = calculate_factorial(5)
# В factorial_result записываем результат функции calculate_factorial(5)
is_even_num = is_even(7)
# В is_even_num записываем результат функции is_even(7)

# Выводим результаты
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")

# Выводим "Число 7 - нечетное." т.к. результат функции False
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")