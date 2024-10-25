'''
Author: Amal Shaji Michael
Date: 25-10-2024
Description: program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
c/5=(f−32)/9

    For Celsius to Fahrenheit conversion:
    f=(95×c)+32

    For Fahrenheit to Celsius conversion:
    c=59×(f−32)

Enter temperature: 100
Is this in (C)elsius or (F)ahrenheit?C
100 Celsius is 212.0 Fahrenheit.

'''


temp=int(input("Enter temperature: "))
scale=input("Is this in (C)elsius or (F)ahrenheit?")
if scale=="C":
    f=(9/5*temp)+32
    print(temp, "Celsius is", f, "Fahrenheit.")
else:
    c = (5/9)*(temp - 32)
    print(temp,"Fahrenheit is", c, "Celsius.")