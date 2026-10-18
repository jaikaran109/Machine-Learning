#Happy Number


n = int(input())
temp = n

while True:
    res = 0

    while temp != 0:
        rem = temp % 10
        res += rem ** 2
        temp //= 10

    if res == 1:
        print("Success")
        break
    if res == 4:
        print("Failed")
        break

    temp = res
