# Q:-55 Print the following Pattern.
# *********
#  *******
#   *****
#    ***
#     *


n = int(input())

for i in range(n, 0, -1):
    for _ in range(0, n - i):
        print(" ", end="")
    for _ in range(0, 2 * i - 1):
        print("*", end="")
    print()
