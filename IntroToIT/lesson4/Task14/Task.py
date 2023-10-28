#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    first_max = max(lst)
    lst.remove(first_max)
    second_max = max(lst)
    return first_max + second_max
#Правильное решение
def wrong_sum_of_two_largest(lst):
    wrong_sum_of_two_largest.sort()
wrong_sum_of_two_largest = wrong_sum_of_two_largest[-2] + wrong_sum_of_two_largest[-1]
print(wrong_sum_of_two_largest)