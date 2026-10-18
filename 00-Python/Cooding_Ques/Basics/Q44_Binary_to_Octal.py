#Write a program to convert any base to any base, like binary to octal.


n = input().strip()
decimal = 0
base = 1

for digit in reversed(n):
    decimal += int(digit) * base
    base *= 2

if decimal == 0:
    print(0)
else:
    digits = []
    while decimal > 0:
        digits.append(str(decimal % 8))
        decimal //= 8
    print("".join(reversed(digits)))
