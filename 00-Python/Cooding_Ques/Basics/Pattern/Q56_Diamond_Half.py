# Q:-56 Print the following Pattern.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


n = 5

for i in range(1, n + 1):
    for _ in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(1, n):
    for _ in range(n - 1, i - 1, -1):
        print("*", end=" ")
    print()
