def fatorial(num):
    if num==1:
        return 1
    else:
        return num*fatorial(num-1)
num1=int(input("Enter the number: "))
print(fatorial(num1))
