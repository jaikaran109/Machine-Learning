# Write a program to find the sum of n natural numbers


n = int(input())

if n > 0:
    total = 0
    for i in range(1, n + 1):
        total += i
    print("Sum of All Natural Number b/w 1 to N is :" + str(total))
else:
    print("Number is Invalid")
