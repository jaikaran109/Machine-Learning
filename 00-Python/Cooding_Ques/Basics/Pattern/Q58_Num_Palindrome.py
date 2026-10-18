# Q:-58 Print the following Pattern.
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321


n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    for _ in range(1, 2 * (n - i) + 1):
        print(" ", end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()
