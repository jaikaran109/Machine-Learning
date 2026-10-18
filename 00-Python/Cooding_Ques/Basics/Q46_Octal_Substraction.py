#Write a program to subtract any base. like the subtraction of two octal values.


def octal_to_decimal(value):
    total = 0
    multiplier = 1
    while value > 0:
        total += (value % 10) * multiplier
        value //= 10
        multiplier *= 8
    return total


def decimal_to_octal(value):
    if value == 0:
        return 0

    result = 0
    multiplier = 1
    while value > 0:
        result += (value % 8) * multiplier
        value //= 8
        multiplier *= 10
    return result


a = int(input())
b = int(input())
decimal1 = octal_to_decimal(a)
decimal2 = octal_to_decimal(b)

if decimal1 >= decimal2:
    diff = decimal1 - decimal2
else:
    diff = decimal2 - decimal1

print(decimal_to_octal(diff))
