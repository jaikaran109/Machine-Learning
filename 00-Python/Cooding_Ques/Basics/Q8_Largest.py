# Java Program to Find Largest Among 3 Numbers


a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(str(a) + " is greater")
elif b > c:
    print(str(b) + " is greater")
else:
    print(str(c) + " is greater")
