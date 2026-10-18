#Swap two numbers without using a temporary variable.


a = int(input())
b = int(input())
a = a + b
b = a - b
a = a - b
print(str(a) + " " + str(b))
