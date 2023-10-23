#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Неправильное решение:
lst = [1, 2, 1, 4, 3, 2, 5]
def wrong_unique_elements(lst):
    new_lst = []
    for item in lst:
        if item in new_lst:
            new_lst.remove(item)
        else:
            new_lst.append(item)
    return new_lst

# Правильное решение:
def correct_unique_elements(lst):
    new_lst = []
    for item in lst:
        if item in new_lst:
            pass
        else:
            new_lst.append(item)
    return new_lst

# Тест
lst = [1, 2, 1, 4, 3, 2, 5]
print(wrong_unique_elements(lst))
print(correct_unique_elements(lst))