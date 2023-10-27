#INTRO TO IT 2nd COURSE
#Задача 8: Подсчет суммы цифр в числе
def sum_of_digits(number):
    cnt = 0
    for x in str(number):
        cnt += int(x)
    return cnt