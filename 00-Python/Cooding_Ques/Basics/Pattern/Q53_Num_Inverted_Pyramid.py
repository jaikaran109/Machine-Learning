# Q:-53 Print the following Pattern.
# 123456
# 12345
# 1234
# 123
# 12
# 1


for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
