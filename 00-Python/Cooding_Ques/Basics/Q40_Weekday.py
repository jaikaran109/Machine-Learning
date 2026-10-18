# Write a Java program that takes a number from the user, number should be an integer between 1 and 7. It displays the weekday name. 
# Input:-3 
# Output:- Wednesday


n = int(input())

if n == 1:
    print("Monday")
elif n == 2:
    print("Tuesday")
elif n == 3:
    print("Wednesday")
elif n == 4:
    print("Thursday")
elif n == 5:
    print("Friday")
elif n == 6:
    print("Saturday")
elif n == 7:
    print("Sunday")
else:
    print("Invalid Day")
