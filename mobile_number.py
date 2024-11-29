def mobile_num(num):
    if len(num)==10 and num[0] in ["9","8","7"]:
        return True
    return False
num1=input("Enter the number: ")
if mobile_num(num1):
    print(f"The mobile number {num1} is valid.")
else:
    print(f"The mobile number {num1} is invalid.")