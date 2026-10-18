# Q:-61 Print the following Pattern.
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A


for i in range(6, 0, -1):
    value = ord("A")
    for _ in range(1, i + 1):
        print(chr(value), end=" ")
        value += 1
    print()
