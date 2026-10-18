# Write a program to convert decimal to any base, like decimal to octal.


print("Enter a decimal number: ", end="")
decimal = int(input())

if decimal == 0:
    print("Octal : 0")
else:
    digits = []

    while decimal > 0:
        remainder = decimal % 8
        digits.append(str(remainder))
        decimal //= 8

    print("Octal : " + "".join(reversed(digits)))
