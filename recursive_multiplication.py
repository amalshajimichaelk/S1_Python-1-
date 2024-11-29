def multiplication(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+multiplication(num1,num2-1)
num1=int(input("Enter the number: "))
num2=int(input("Enter the number: "))
print(f"The Product: {multiplication(num1,num2)}")