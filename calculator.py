'''
Author: Amal Shaji Michael
Date: 19-18-2024
Description:program that performs the following tasks:

    User Input,Addition,Subtraction,
    Multiplication, Division,
    Modulus,Combined Arithmetic Operation

    Enter the first number:2
Enter the second number:4
Enter the third number:6
The sum of num1 and num2 is 6
The difference when num2 is subtracted from num1 is 2
The product of num1 and num2 is 8
The quotient when num1 is divided by num2 is 0.5
The remainder when num1 is divided by num2 is 2
The result of (num1 + num2) * num3 / 2 is 18.0

'''


num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
print("The sum of num1 and num2 is", num1+num2)
print("The difference when num2 is subtracted from num1 is", num2-num1)
print("The product of num1 and num2 is", num1*num2)
print("The quotient when num1 is divided by num2 is", num1/num2)
print("The remainder when num1 is divided by num2 is", num1%num2)
print("The result of (num1 + num2) * num3 / 2 is", (num1+num2)*num3/2)

