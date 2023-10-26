#INTRO TO IT 2nd COURSE
#Задача 8: Подсчет суммы цифр в числе
def sum_of_digits(number):
    digits = [int(i) for i in str(number)]
    return sum(digits)