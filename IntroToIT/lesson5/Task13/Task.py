#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:
def wrong_is_sorted(lst, key=lam x: x):
    for i, el in enumerate(lst[1:] ):
        if key(el) < key(lst[i]):
            return False
    return True