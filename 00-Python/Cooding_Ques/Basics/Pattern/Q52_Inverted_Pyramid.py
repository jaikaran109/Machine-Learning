# Q:-52 Print the following Pattern.
# ******
# *****
# ****
# ***
# **
# *


for i in range(6, 0, -1):
    for _ in range(i, 0, -1):
        print("*", end="")
    print()
