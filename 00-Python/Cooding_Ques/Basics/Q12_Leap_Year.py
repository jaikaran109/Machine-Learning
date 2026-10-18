# Java Program to Check Leap Year


n = int(input())

if (n % 100 != 0 and n % 4 == 0) or n % 400 == 0:
    print("Year is Leap Year")
else:
    print("Not a Leap Year")
