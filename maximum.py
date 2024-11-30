def maximum(l):
    l.sort()
    print(f"the maximum of three numbers {l[2]}")
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
num3= int(input("Enter third number: "))
l = [num1,num2,num3]
maximum(l)