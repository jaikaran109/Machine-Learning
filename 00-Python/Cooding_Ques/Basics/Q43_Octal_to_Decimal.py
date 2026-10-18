#Write a program to convert any base to decimal, like octal to decimal.


n = input().strip()
x = 1
ans = 0

for digit in reversed(n):
    ans += int(digit) * x
    x *= 8

print(ans)
