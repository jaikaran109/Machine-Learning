# How to Reverse a Number in Java


num = int(input())
rev = 0

while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

print(rev)
