# lösning 1 biljettpris
# age = int(input("Please state your age: "))

# if age >= 0 and age <= 3:
#     print("free")
# elif age >= 4 and age <= 12:
#     print("8$")
# elif age >= 13 and age <= 59:
#     print("12$")
# elif age >= 60:
#     print("6$")
# else:
#     print("error fucker")
    
# # Tobias lösning
# age = (input("Please state your age: "))


    
# Lösning 2 Rock paper scissors

import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

user_choice = input("Rock, paper or scissors?: ").lower()

if user_choice not in choices:
        print("please pick one of rock, paper and scissors")
else:
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
                print("It's a tie")
                        
        elif user_choice == "rock" and computer_choice == "scissors":
                print("rock beats scissors, You win")
                
        elif user_choice == "paper" and computer_choice == "rock":
                print("paper beats rock, you win")
                        
        elif user_choice == "scissors" and computer_choice == "paper":
                print("scissors beats paper, you win")
                        
        else:
                print("You lose")

# KOMMENTERA och förbättra

#yo 