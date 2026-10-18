# Java Program to Check if a Given Number is Perfect Square


print("Enter Your Number")
num = int(input())
sqrt = int(num ** 0.5)

if sqrt * sqrt == num:
    print("perfect Square " + str(sqrt))
else:
    print("The Number Not have perfect square root")
