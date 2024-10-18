'''
Author: Amal Shaji Michael
Date: 18-18-2024
Description: program that uses functions from the math module to perform
 the following operations on a number provided by the user:
     Find the square root.
    Calculate the factorial.
    Raise the number to the power of 2.
    Enter your number:2
Square root of 2 : 1.4142135623730951
Factorail of 2 : 2
2 to the power of 2 :  4.0
'''


import math
number1=int(input("Enter your number:"))
square_root=(math.sqrt(number1))
print("Square root of",number1, ":", square_root)
factorial=(math.factorial(number1))
print("Factorail of", number1, ":", factorial)
power=(math.pow(number1,2))
print(number1,"to the power of 2 : ", power)