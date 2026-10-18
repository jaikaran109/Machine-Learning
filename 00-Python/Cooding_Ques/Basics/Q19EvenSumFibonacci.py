# Java Program to Find Even Sum of Fibonacci Series Till number N


n = int(input())
a = 0
b = 1
total = 0

for _ in range(1, n + 1):
    if a % 2 == 0:
        total += a
    next_value = a + b
    a = b
    b = next_value

print(total)
