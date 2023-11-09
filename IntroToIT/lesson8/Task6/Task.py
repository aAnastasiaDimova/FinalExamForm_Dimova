#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    reversed_s = ''
    for i in range(1, len(s)+1):
        reversed_s +=s[-i] 
    return reversed_s
