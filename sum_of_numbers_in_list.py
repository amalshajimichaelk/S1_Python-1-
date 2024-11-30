def list_sum(list):
    sum=0
    for i in list:
        sum=sum+i
    print(f"The sum: {sum}")
list=[]
n= int(input("Enter the no.of elements: "))
for i in range(n):
    m=int(input("Enter the elements :"))
    list.append(m)
print(list)
list_sum(list)