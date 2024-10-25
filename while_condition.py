'''
Author: Amal Shaji Michael
Date: 25-10-2024
Description: program to find the sum of the digits of the number entered.

Enter a number:123
Sum of digits of the given number: 6

'''


number=int(input("Enter a number:"))
sum_of_digits=0
while number>0:
    remainder=number%10
    sum_of_digits=sum_of_digits+remainder
    number=number//10
print("Sum of digits of the given number:", sum_of_digits)
