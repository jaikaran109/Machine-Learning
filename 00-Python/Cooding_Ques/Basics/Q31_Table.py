# Write a Java program that takes a number as input and prints its multiplication table up to 10. 
# TInput a number: 8 
# Expected Output: 8 x 1 = 8 8 x 2 = 16 8 x 3 = 24 ... 8 x 10 = 80


n = int(input())
print("Table of n is :")

for i in range(1, 11):
    print(str(n) + " * " + str(i) + " = " + str(n * i))
