# Java Program to Check whether the input number is a Neon Number.


a = int(input())
b = a * a
res = 0

while b != 0:
    res += b % 10
    b //= 10

if res == a:
    print("Number is Neon Number")
else:
    print("its Not")
