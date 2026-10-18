# Write a Java program to find the number of days in a month. 
# Input a month:- 2 
# Input a year: 2016 
# Expected Output:- February 2016 has 29 days. 
#ANOTHER METHOD
# import java.util.Scanner;
# public class Q41 {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);
#         // Input month and year
#         System.out.print("Input a month (1-12): ");
#         int month = sc.nextInt();
#         System.out.print("Input a year: ");
#         int year = sc.nextInt();
#         int days;
#         switch (month) {
#             case 1: case 3: case 5: case 7: case 8: case 10: case 12:
#                 days = 31;
#                 break;
#             case 4: case 6: case 9: case 11:
#                 days = 30;
#                 break;
#             case 2:
#                 // Leap year check
#                 if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
#                     days = 29;
#                 } else {
#                     days = 28;
#                 }
#                 break;
#             default:
#                 System.out.println("Invalid month.");
#                 return;
#         }
#         String[] monthNames = {
#             "", "January", "February", "March", "April", "May", "June",
#             "July", "August", "September", "October", "November", "December"
#         };
#         System.out.println(monthNames[month] + " " + year + " has " + days + " days.");
#     }
# }


print("Enter Your Year :")
year = int(input())

print("Enter Your Month :")
month = int(input())

if month == 1:
    print("January " + str(year) + " has :" + str(31) + " days")
elif month == 2:
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        feb = 29
    else:
        feb = 28
    print("February " + str(year) + " has :" + str(feb) + " days")
elif month == 3:
    print("March " + str(year) + " has :" + str(31) + " days")
elif month == 4:
    print("April " + str(year) + " has :" + str(30) + " days")
elif month == 5:
    print("May " + str(year) + " has :" + str(31) + " days")
elif month == 6:
    print("June " + str(year) + " has :" + str(30) + " days")
elif month == 7:
    print("July " + str(year) + " has :" + str(31) + " days")
elif month == 8:
    print("August " + str(year) + " has :" + str(31) + " days")
elif month == 9:
    print("September " + str(year) + " has :" + str(30) + " days")
elif month == 10:
    print("October " + str(year) + " has :" + str(31) + " days")
elif month == 11:
    print("November " + str(year) + " has :" + str(30) + " days")
elif month == 12:
    print("December " + str(year) + " has :" + str(31) + " days")
else:
    print("Invalid Month")
