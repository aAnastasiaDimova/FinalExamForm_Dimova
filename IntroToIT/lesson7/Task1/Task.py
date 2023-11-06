#INTRO TO IT 2nd COURSE

# Функция для сложения двух чисел a и b
def add_numbers(a, b):
    # сложение чисел и занесение их в переменную result
    result = a + b
    # возвращение суммы чисел
    return result

# Функция для умножения двух чисел a и b
def multiply_numbers(a, b):
    # умножение чисел и занесение их в переменную result
    result = a * b
    # возвращение произведения чисел
    return result

# Функция для нахождения наибольшего числа в списке numbers
def find_max_number(numbers):
    # нахождение максимального числа
    max_number = max(numbers)
    # возвращение максимального числа
    return max_number

# Функция для вычисления факториала числа n
def calculate_factorial(n):
    # если n = 0, то факториал равен 1
    if n == 0:
        return 1
    # переменная factorial хранит вычисления факториала
    factorial = 1
    # цикл for проходит от 1 до n + 1
    for i in range(1, n + 1):
        #умнжаем factorial на i 
        factorial *= i
    # возвращаем факториал числа n
    return factorial

# Функция для проверки четности числа
def is_even(number):
    # если при делении на 2 остаток 0
    if number % 2 == 0:
        #возвращаем True
        return True
    # если остаток от делеения не 0
    else:
        # возвращаем False
        return False
# присваиваем переменной num1 значение 10
num1 = 10
# присваиваем переменной num2 значение 5
num2 = 5
# переменная sum_result содержит результат сложения num1 и num2
sum_result = add_numbers(num1, num2)
# переменная product_result содержит результат умножения num1 и num2
product_result = multiply_numbers(num1, num2)
#переменная numbers_list содержит список чисел
numbers_list = [3, 8, 1, 6, 12]
# переменная max_num содержит наибольшее число из списка numbers_list
max_num = find_max_number(numbers_list)
#переменная factorial_result содержит результат вычисления факториала числа 5
factorial_result = calculate_factorial(5)
# переменная is_even_num содержит результат проверки, является ли число 7 четным
is_even_num = is_even(7)
#вывод результатов выполнения функция и проверок
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")