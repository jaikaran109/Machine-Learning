# Java Program to Check Palindrome given number.


n = int(input())
b = n
rev = 0

while n != 0:
    a = n % 10
    rev = rev * 10 + a
    n //= 10

if b == rev:
    print("it's palindrome")
else:
    print("it's Not")
