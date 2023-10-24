#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Неправильное решение:
def f(l):
    n = []
    for i in l:
        if i not in n:
            n.remove(i)
        else:
            n.append(i)
    return n