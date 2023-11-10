#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    a = list(set(numbers))
    a.sort()
    return a[-2]
    

print(second_largest([10, 4, 9, 4, 9, 10, 4]))  # Должно вывести 9
