#Check Sum Of Factor Is Equal To Number


n = int(input())
sum_of_factors = 1
temp = n

for i in range(2, n):
    if temp % i == 0:
        sum_of_factors += i

if sum_of_factors == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
