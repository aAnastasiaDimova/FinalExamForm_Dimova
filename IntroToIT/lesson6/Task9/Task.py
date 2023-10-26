#INTRO TO IT 2nd COURSE
# Задача 9: Переворот строки
def reverse_string(s):
    res=''
    for i in range(len(s)-1,-1,-1):
        res+=s[i]
    return res

n = reverse_string(input())
print(n)