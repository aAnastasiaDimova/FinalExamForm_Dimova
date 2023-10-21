#INTRO TO IT 2nd COURSE

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
print("Factorial of a number:", factorial(number))
