#INTRO TO IT 2nd COURSE
#Задача 10: Вычисление факториала
def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return n
    elif n > 1:
        return n * factorial(n-1)
    
    
print(factorial(5))