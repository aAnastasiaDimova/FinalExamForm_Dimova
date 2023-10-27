#INTRO TO IT 2nd COURSE
#Задача 10: Вычисление факториала
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)