def gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
print(f"The GCD: {gcd(n1,n2)}")