#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    first = second = float('-inf')
    for n in numbers:
        if n > first:
            x = first
            first = n
            second = x
        elif n > second:
            second = n
        
    return second if second != float('-inf') else None

print(second_largest([4, 9, 4, 9, 10, 4]))  # Должно вывести 9
