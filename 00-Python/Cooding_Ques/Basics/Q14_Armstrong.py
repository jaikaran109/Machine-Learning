# Java Program to Check Armstrong Number between Two Integers
#IMPORTANT


print("Enter your first limit")
limit1 = int(input())

print("Enter your Second limit")
limit2 = int(input())

print("Armstrong number Between " + str(limit1) + " and " + str(limit2))

for num in range(limit1, limit2 + 1):
    temp = num
    count_digit = 0

    while temp != 0:
        count_digit += 1
        temp //= 10

    temp = num
    arm = 0

    while temp != 0:
        rem = temp % 10
        arm += rem ** count_digit
        temp //= 10

    if arm == num:
        print(arm)
