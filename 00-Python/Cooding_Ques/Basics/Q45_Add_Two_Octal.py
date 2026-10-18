#Write a program to add to any base. like the addition of two octal values.


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
total = octal_to_decimal(a) + octal_to_decimal(b)
print(decimal_to_octal(total))
