# Q:-63 Print the following Pattern.
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1


n = int(input())

for i in range(n, 0, -1):
    for j in range(n, i - 1, -1):
        print(str(j) + " ", end="")
    print()
