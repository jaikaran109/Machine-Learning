def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input())
temp = n
res = 0

while temp != 0:
    rem = temp % 10
    res += fact(rem)
    temp //= 10

if n == res:
    print("Yes it's Strong Number ")
else:
    print("No , not strong Number")
