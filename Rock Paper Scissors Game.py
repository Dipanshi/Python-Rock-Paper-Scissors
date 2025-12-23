print("Welcome to Rock, Paper, Scissors Game!")
import random
choices = ["rock", "paper", "scissors"]
user_wins=0
computer_wins=0

while True:
    user_choice = input("Enter rock, paper, scissors or Q to quit:").lower()
    if user_choice == 'q':
        print("Thanks for Playing! Good Bye!")
        quit()
    if user_choice in choices:
        computer_choice= random.choice(choices)
        print("Computer chose:", computer_choice)
        if user_choice == "rock" and computer_choice == "scissors":
            print("You win! Rock crushes Scissors")
            user_wins += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win! Paper covers Rock")
            user_wins += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win! Scissors cut Paper")
            user_wins += 1
        elif user_choice == computer_choice:
            print("It's a tie!")
        else:
            print("Computer wins!")
            computer_wins += 1
      
    else:
        print("Invalid choice. Please try again.")

    print("Score: You -", user_wins, "Computer -", computer_wins)

    if user_wins> computer_wins:
        print("Congratulations! You are leading the game.")
    elif computer_wins> user_wins:
        print("Computer is leading the game. Try harder!")
    else:
        print("The game is currently tied.")