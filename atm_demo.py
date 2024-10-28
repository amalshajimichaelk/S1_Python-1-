'''
Amal Shaji Michael
Date: 28-10-2024
Description: program that simulates a simple bank ATM system.
The user has an initial balance of $1000.
The ATM should display a menu with options to:

    Check Balance
    Deposit Money
    Withdraw Money
    Exit

    1.	Check Balance
2.	Deposit Money
3.	Withdraw Money
4.	Exit
Enter your choice: 1
The current balance: $1000

1.	Check Balance
2.	Deposit Money
3.	Withdraw Money
4.	Exit
Enter your choice: 2
Enter the amount: 300
The deposit amount: $300.0 and the current balance: $1300.0

1.	Check Balance
2.	Deposit Money
3.	Withdraw Money
4.	Exit
Enter your choice: 3
Enter the amount to withdraw: 4000
Insufficient Balance

1.	Check Balance
2.	Deposit Money
3.	Withdraw Money
4.	Exit
Enter your choice: 300
Invalid Entry

1.	Check Balance
2.	Deposit Money
3.	Withdraw Money
4.	Exit
Enter your choice: 3
Enter the amount to withdraw: 300
The withdraw amount: $300.0 and The current balance: $1000.0

1.	Check Balance
2.	Deposit Money
3.	Withdraw Money
4.	Exit
Enter your choice: 4

Process finished with exit code 0

'''


balance_amount=1000
while True:
    print("\n1.\tCheck Balance")
    print("2.\tDeposit Money")
    print("3.\tWithdraw Money")
    print("4.\tExit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print(f"The current balance: ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("Enter the amount: "))
        balance_amount=balance_amount+deposit_amount
        print(f"The deposit amount: ${deposit_amount} and " 
              f"the current balance: ${balance_amount}")
    elif choice==3:
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount>balance_amount:
            print("Insufficient Balance")
        else:
             balance_amount = balance_amount - withdraw_amount
             print(f"The withdraw amount: ${withdraw_amount} and "
              f"The current balance: ${balance_amount}")
    elif choice==4:
        break
    else:
        print("Invalid Entry")