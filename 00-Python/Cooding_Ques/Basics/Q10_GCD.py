# Java Program to Find GCD or HCF of 2 numbers


a = int(input())
b = int(input())

while b != 0:
    rem = a % b
    a = b
    b = rem

print("GCD = " + str(a))
