'''
Amal Shaji Michael
Date: 28-10-2024
Description: program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:

    Convert Celsius to Fahrenheit
    Convert Fahrenheit to Celsius
    Exit the program




1.	Enter a temperature in Celsius
2.	Enter a temperature in Fahrenheit
3.	Exit
Enter your choice: 1
Enter a temperature in Celsius: 100
The temnperature in Fahrenheit: 212.0 degree Fahrenheit

1.	Enter a temperature in Celsius
2.	Enter a temperature in Fahrenheit
3.	Exit
Enter your choice: 2
Enter a temperature in Fahrenheit: 32
The temoperature in Celsius: 0.0 degree Celsius

1.	Enter a temperature in Celsius
2.	Enter a temperature in Fahrenheit
3.	Exit
Enter your choice: 4
Invalid Entry

1.	Enter a temperature in Celsius
2.	Enter a temperature in Fahrenheit
3.	Exit
Enter your choice: 3

Process finished with exit code 0

'''


while True:
    print("\n1.\tEnter a temperature in Celsius")
    print("2.\tEnter a temperature in Fahrenheit")
    print("3.\tExit")
    choice=int(input("Enter your choice: "))
    if choice==1:
       celsius=int(input("Enter a temperature in Celsius: "))
       fahrenheit = (celsius*(9 / 5) + 32)
       print(f"The temnperature in Fahrenheit: {fahrenheit} degree Fahrenheit ")
    elif choice==2:
        fahrenheit_input=int(input("Enter a temperature in Fahrenheit: "))
        celsius_output=(fahrenheit_input - 32) * 5/9
        print(f"The temoperature in Celsius: {celsius_output} degree Celsius")
    elif choice==3:
        break
    else:
        print("Invalid Entry")
