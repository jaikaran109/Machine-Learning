# Write a Java program to print the area and perimeter of a circle. 
# Test Data: Radius = 7.5 
# Area is = 176.71458676442586 
# Expected Output Perimeter is = 47.12388980384689


import math


radius = float(input())
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius

print("Perimeter is = " + str(perimeter))
print("Area is = " + str(area))
