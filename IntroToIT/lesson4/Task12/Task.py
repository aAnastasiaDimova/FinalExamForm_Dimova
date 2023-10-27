#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Неправильное решение:
def wrong_unique_elements(lst):
     for item in lst:
        if item in lst:
            lst.remove(item)
        else:
            lst.append(item)
    return lst
