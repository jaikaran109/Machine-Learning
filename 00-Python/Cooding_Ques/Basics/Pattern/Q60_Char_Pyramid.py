# Q:-60 Print the following Pattern.
# A
# A B
# A B C
# A B C D
# A B C D E
# A B C D E F


for i in range(1, 7):
    value = ord("A")
    for _ in range(1, i + 1):
        print(chr(value), end=" ")
        value += 1
    print()
