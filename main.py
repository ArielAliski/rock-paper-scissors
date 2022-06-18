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

choice = int(input("What do you choose? Type 0 for rock, Type 1 for paper, or Type 2 for scissors: "))
computer_choice = random.randint(0,2)
#Battle Animation Start
print("You have chosen: ")
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
else:
  print("Not a valid choice")
if choice > 2:
  print("Game has been terminated due to invalid choice")
  exit() 
print("Computer have chosen: ")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)
else:
  print("Not a valid choice")
#Battle Animation End

#Winning decider start

#if person chooses rock
if choice == 0 and computer_choice == 0:
  print("You tied!")
if choice == 0 and computer_choice == 1:
  print("You lose :(")
if choice == 0 and computer_choice == 2:
  print("You Win!")

  #if person chooses paper
if choice == 1 and computer_choice == 1:
  print("You tied!")
if choice == 1 and computer_choice == 2:
  print("You lose :(")
if choice == 1 and computer_choice == 0:
  print("You Win!")

    #if person chooses scissors
if choice == 2 and computer_choice == 2:
  print("You tied!")
if choice == 2 and computer_choice == 0:
  print("You lose :(")
if choice == 2 and computer_choice == 1:
  print("You Win!")
