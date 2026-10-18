# Q:-59 Print the following Pattern.
#
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15


n = int(input())
count = 1

for i in range(1, n + 1):
    for _ in range(1, i + 1):
        print(str(count) + " ", end="")
        count += 1
    print()
