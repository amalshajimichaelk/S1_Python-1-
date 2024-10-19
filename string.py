'''
Author: Amal Shaji Michael
Date: 19-18-2024
Description:program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between
    and store the result in a new variable.

    Print the concatenated string.

    From the concatenated string:
        Access and print a sub-string that consists of the last name only.
        Use string slicing to extract the sub-string.

Enter your first name:Amal
Enter your last name:Shaji Michael
Amal Shaji Michael
4
 Shaji Michael

'''


string1=(str(input("Enter your first name:")))
string2=(str(input("Enter your last name:")))
name=(string1+" "+string2)
print(name)
length=len(string1)
print(length)
extracted_string1=name[length:]
print(extracted_string1)

