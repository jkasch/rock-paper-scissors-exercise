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

#Write your code below this line 👇
import random

player_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if player_input != "0" or "1" or "2":
  print("You typed an invalid number.")
elif player_input == "0":
  print(rock)
elif player_input == "1":
  print(paper)
elif player_input == "2":
  print(scissors)

print ("Computer chose:")
computer_choice = random.choice([rock, paper, scissors])
print(computer_choice)

if player_input != "0" or "1" or "2":
  print("Computer wins!")
elif player_input == "0":
  if computer_choice == rock:
    print("It's a tie! Rematch.")
  elif computer_choice == paper:
    print("You lose!")
  elif computer_choice == scissors:
    print("You win!")
elif player_input == "1":
  if computer_choice == rock:
    print("You win!")
  elif computer_choice == paper:
    print("It's a tie! Rematch!")
  elif computer_choice == scissors:
    print("You lose!")
elif player_input == "2":
  if computer_choice == rock:
    print("You lose!")
  elif computer_choice == paper:
    print("You win!")
  elif computer_choice == scissors:
    print("It's a tie! Rematch!")