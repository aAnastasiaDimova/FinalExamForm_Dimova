#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    lst2 = sum(sorted(lst, reverse=True)[0:2])
    return lst2