
print("---WELCOME TO THE GAME---")
import random

user = input("Choose rock, paper, or scissors: ").lower()
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

print("Your choice is", user)
print("Computer choice:", computer)

if user == computer:
    print("GAME DRAW")
elif user == "rock" and computer == "scissors":
    print("YOU WON!")
elif user == "paper" and computer == "rock":
    print("YOU WON!")
elif user == "scissors" and computer == "paper":
    print("YOU WON!")
elif user in choices:
    print("BETTER LUCK NEXT TIME!")
else:
    print("INVALID INPUT!")


