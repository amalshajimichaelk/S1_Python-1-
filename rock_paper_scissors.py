import random
options=['rock','paper','scissors']
while True:
    player_choice = input("Enter rock, paper or scissors (or quit to exit): ")
    computer_choice = random.choice(options)
    if player_choice=='quit':
        break
    if player_choice==computer_choice:
        print("Congrats! You have a Tie")
    elif computer_choice=='paper' and player_choice=='scissors':
        print("You Wins!")
    elif computer_choice=='scissors' and player_choice=='rock':
        print("You Wins!")
    elif computer_choice=='rock' and player_choice=='paper':
        print("You Wins!")
    else:
        print("You lose")

