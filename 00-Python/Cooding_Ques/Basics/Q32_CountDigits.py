# write a program to count number of digits present in a given integer value. 
# Input:-123
# Output-3


n = abs(int(input()))
count = 0

if n == 0:
    count = 1
else:
    while n != 0:
        count += 1
        n //= 10

print(count)
