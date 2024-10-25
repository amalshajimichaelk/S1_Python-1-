'''
Author: Amal Shaji Michael
Date: 25-10-2024
Description: A program to find whether the number entered is positive,
negative or zero.

Enter the number: 0
The number, 0  is zero.
'''


number=int(input("Enter the number: "))
if number>0:
    print("The number, ", number, " is positive.")
elif number<0:
    print("The number, ",number, " is negative.")
else:
    print("The number,", number, " is zero.")