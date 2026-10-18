# Q:-51 Print the following Pattern.
# 1
# 22
# 333
# 4444
# 55555
# 666666


for i in range(1, 7):
    for _ in range(1, i + 1):
        print(i, end="")
    print()
