# Java Program to Calculate the Power of a Number:


base = int(input())
power = int(input())
result = 1

for _ in range(1, power + 1):
    result *= base

print(result)
