# Write a program to print all digits of a given integer value. 
# Input:-123
# Output-3
#        2
#        1


n = abs(int(input()))

if n == 0:
    print(0)
else:
    while n != 0:
        print(n % 10)
        n //= 10
