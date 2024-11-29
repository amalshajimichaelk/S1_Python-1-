def add_numbers(num1,num2):
    if num2==0:
        return num1
    else:
        return add_numbers(num1+1,num2-1)
n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
print(f"The sum: {add_numbers(n1,n2)}")