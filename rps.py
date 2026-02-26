import random
from colorama import init, Fore
init(autoreset=True)

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors!")

while True:
    
    player = input("Choose rock, paper, or scissors: ").lower()

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == "rock" and computer == "scissors":
        print("You win rock star!")
    elif player == computer:
        print("It's a tie!")
    elif player == "scissors" and computer == "paper":
        print("You are really cutting down your opponent! You win!")
    elif player == "paper" and computer == "rock":
        print("You win! You are a paper champion!")
    else:
        print("You lose! Better luck next time!")

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break

        

