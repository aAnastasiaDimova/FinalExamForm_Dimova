#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def sum_of_two_largest(lst):
    lst = set(lst)
    first_max = max(lst)
    lst.remove(max(lst))
    second_max = max(lst)
    return first_max + second_max
