# Q:-64 Print the following Pattern.
# E
# E F
# E F E
# E F E D
# E F E D C
#input must be b/w 1 to 15


n = int(input())
arr = ["E", "F", "E", "D", "C"]

for i in range(n):
    for j in range(i + 1):
        print(arr[j], end=" ")
    print()
