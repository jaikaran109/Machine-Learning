# Q:-65 Print the following Pattern.
#      A
#     ABA
#    ABCBA
#   ABCDCBA
#  ABCDEDCBA


for i in range(1, 6):
    for _ in range(5, i, -1):
        print(" ", end="")

    ch = ord("A")
    for _ in range(1, i + 1):
        print(chr(ch), end="")
        ch += 1

    ch -= 2
    for _ in range(1, i):
        print(chr(ch), end="")
        ch -= 1

    print()
