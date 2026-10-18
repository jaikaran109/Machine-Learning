# Java Program to Add Two Binary Strings
# Have a look *


print("Enter first binary string: ", end="")
bin1 = input().strip()

print("Enter second binary string: ", end="")
bin2 = input().strip()

num1 = int(bin1, 2)
num2 = int(bin2, 2)
total = num1 + num2
result = format(total, "b")

print("Sum of binary strings: " + result)
