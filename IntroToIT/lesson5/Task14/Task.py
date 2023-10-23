#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    first_max = max(lst)
    lst.remove(first_max)
    second_max = max(lst)
    return first_max + second_max

# Правильное решение:
def correct_sum_of_two_largest(lst):
    lst.sort(reverse=True)
    first_max = lst[0]
    second_max = lst[1]
    return first_max + second_max

# Тест
lst_w = [1, 2, 3, 4]
lst_c = [1, 2, 3, 4]
print(wrong_sum_of_two_largest(lst_w))
print(correct_sum_of_two_largest(lst_c))
