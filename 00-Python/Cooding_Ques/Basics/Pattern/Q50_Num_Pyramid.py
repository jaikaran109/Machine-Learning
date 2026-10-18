# Q:-50 Print the following Pattern.
# 1
# 12
# 123
# 1234
# 12345


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
