# Java Program to Find LCM of 2 numbers


def least(a, b):
    return a if a < b else b


a = int(input())
b = int(input())

x = a
y = b
lcm = 1
i = 2
least_value = least(a, b)

while i <= least_value:
    if x % i == 0 and y % i == 0:
        lcm *= i
        x //= i
        y //= i
    else:
        i += 1

lcm = lcm * x * y
print(lcm)
