#INTRO TO IT 2nd COURSE
# Задача: проверить, является ли число простым
import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1): # верхняя граница в цикле не правильная
        if num % i == 0:
            return False
        return True 