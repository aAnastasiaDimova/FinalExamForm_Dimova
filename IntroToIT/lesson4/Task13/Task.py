#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:
def wrong_is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return True
    return False
#Правильное решение (ну а, способо другой же))))
from itertools import imap, tee
import operator

def wrong_is_sorted(iterable, compare=operator.le):
  a, b = tee(iterable)
  next(b, None)
  return all(imap(compare, a, b))