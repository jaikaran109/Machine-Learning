# Print the following Pattern.
#******
#*    *
#*    *
#*    *
#******


n = int(input())
m = int(input())

for i in range(0, n + 1):
    for j in range(0, m + 1):
        if i == 0 or j == 0 or i == n or j == m:
            print("*", end="")
        else:
            print(" ", end="")
    print()
