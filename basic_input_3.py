'''
Author: Amal Shaji Michael
Date: 18-18-2024
Description: program that demonstrates the usage of arithmetic, comparison, and logical operators.
 Perform a few operations and print the results.
 Enter the first number:2
Enter the second number:2
Sum 4 Division= 1.0
Is number1 greater than number2? False
Are number1 and number2 equal? True
Logical AND: True
Logical OR: True



'''


number1 =int(input("Enter the first number:"))
number2 =int(input("Enter the second number:"))
print("Sum" ,number1+number2, "Division=" ,number1/number2)
print("Is number1 greater than number2?", number1>number2)
print("Are number1 and number2 equal?", number1==number2)
print("Logical AND:", number1>0 and number2>0)
print("Logical OR:", number1>0 or number2>number1)

