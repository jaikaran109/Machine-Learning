# Write a Java program and compute the sum of an integer's digits. Input Data: Input an integer: 25 Expected Output 
# The sum of the digits is: 7


n = abs(int(input()))
total = 0

while n != 0:
    total += n % 10
    n //= 10

print("The Sum of Digits is :" + str(total))
