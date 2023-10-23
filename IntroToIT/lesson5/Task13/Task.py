#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:
def wrong_is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return True
    return False

# Неправильное решение:
def correct_is_sorted(lst):
    Check = True
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            pass
        else:
            Check = False
            break
    return Check

# Тест
lst = [1, 5, 3, 5, 4]
print(wrong_is_sorted(lst))
print(correct_is_sorted(lst))