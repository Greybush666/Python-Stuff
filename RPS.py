rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

hands = [rock, paper, scissors]

user_choice = int(input(" What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

if user_choice >= 3 or user_choice < 0:
  print("You fucked up")
else: 
  print(hands[user_choice])

  computer_choice = random.randint (0, 2)
  print("Computer chose: ")
  print(hands[computer_choice])

  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice > user_choice:
    print("You lose!")
  elif computer_choice == user_choice:
    print("FUCKING DRAW")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose retard")
  elif user_choice > computer_choice:
    print("You win!")
