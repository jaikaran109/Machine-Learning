# Q:-67 Print the following Pattern.
#*                 * 
#* *             * * 
#* * *         * * * 
#* * * *     * * * * 
#* * * * * * * * * * 
#* * * * * * * * * * 
#* * * *     * * * * 
#* * *         * * * 
#* *             * * 
#*                 *


n = int(input())

for i in range(1, n + 1):
    for _ in range(1, i + 1):
        print("*", end=" ")
    for _ in range(2 * (n - i), 0, -1):
        print("  ", end="")
    for _ in range(1, i + 1):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for _ in range(i, 0, -1):
        print("*", end=" ")
    for _ in range(2 * (n - i), 0, -1):
        print("  ", end="")
    for _ in range(i, 0, -1):
        print("*", end=" ")
    print()
