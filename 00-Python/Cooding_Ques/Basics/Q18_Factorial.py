# Java Program to Find Factorial of a number


n = int(input())
fact = 1

if n == 0:
    print("Factorial is :1")
else:
    for i in range(n, 0, -1):
        fact *= i
    print("Factorial is :" + str(fact))
