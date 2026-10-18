#Check Armstrong
#			res += Math.pow(rem, count);


n = int(input())
temp = n
rem = 0
res = 0
count = 0

while temp != 0:
    count += 1
    temp //= 10

temp = n
while temp != 0:
    rem = temp % 10
    res1 = 1
    for _ in range(count):
        res1 *= rem
    res += res1
    temp //= 10

if n == res:
    print("Armstrong")
else:
    print("Not Armstrong")
