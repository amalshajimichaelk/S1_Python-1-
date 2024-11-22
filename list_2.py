'''                                                                               
 Author:Amal Shaji Michael                                                        
 Date: 22-11-2024                                                                 
 Description:Program which input two lists from the user. 
 Merge these lists into a third list such that in the merged list,
 all even numbers occur first followed by odd numbers. 
 Both the even numbers and odd numbers should be in sorted order.
'''                                                                               
list_1=[12,21,54,47,88,67]
list_2=[20,13,34,5,66,91]
combined_list=list_1+list_2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
combined_list=even_list+odd_list
print(f"Even number list: {even_list}")
print(f"Odd number list: {odd_list}")
print(f"Combined list: {combined_list}")
