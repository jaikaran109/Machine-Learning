# Q:-62 Print the following Pattern.
# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F


value = ord("A")

for i in range(1, 7):
    for _ in range(1, i + 1):
        print(chr(value), end=" ")
    value += 1
    print()
