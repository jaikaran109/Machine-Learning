# Write a program to print a particular digit in a given position from given integer value. 
# Input:-123456
#             2
# Output-5


print("Enter Your Number :")
n = int(input())
temp = abs(n)
count = 0

print("Enter position ")
position = int(input())

if temp == 0:
    count = 1
else:
    while temp != 0:
        count += 1
        temp //= 10

if position <= 0 or position > count:
    print("Invalid Position / Out Of Range ")
else:
    number = abs(n)
    for _ in range(1, position):
        number //= 10
    digit = number % 10
    print(digit)
