# Q:-54 Print the following Pattern.
#     *
#    ***
#   *****
#  *******
# *********
# VIA WHILE LOOOP
# public class Q54 {
#     public static void main(String[] args) {
#         int n = 5 ; 
#         int space = n - 1 ; 
#         int star = 1 ;
#         int i = 1 ; 
#         while(i <= n)
#         {
#             int k  = 1;
#             while(k <= space)
#             {
#                 System.out.print("  ");
#                 k++ ;
#             }
#             int j = 1 ; 
#             while(j <= star)
#             {
#                 System.out.print("* ");
#                 j++ ;
#             } 
#             star+=2 ;
#             space-- ;
#             System.out.println();
#             i++ ;
#         }
#     }
# }
# // Via for loop


for i in range(1, 6):
    for _ in range(5 - i, 0, -1):
        print(" ", end="")
    for _ in range(1, 2 * i):
        print("*", end="")
    print()
