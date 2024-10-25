'''
Author: Amal Shaji Michael
Date: 25-10-2024
Description: Write a Python program to find the largest of three numbers.
The program should take three numbers as input from the user and determine which one is the largest.
 Use conditional statements to compare the numbers.

 Enter the first number: 1
Enter the second number: 2
Enter the third number: 3
3  is greater than other two.

'''


number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the third number: "))
if number1>number2 and number1>number3:
    print(number1, "is greater than the other two.")
elif number2>number1 and number2>number3:
    print(number2," is greater than other two.")
else:
    print(number3, " is greater than other two.")