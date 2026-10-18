# Java Program to Find Quotient and Remainder:


dividend = int(input())
divisor = int(input())

if divisor == 0:
    print("Division by zero not allowed")
else:
    quotient = dividend // divisor
    remainder = dividend % divisor
    print("Quotient: " + str(quotient))
    print("Remainder: " + str(remainder))
