# Author: Irene Buck
# Date: 7/20/23
# Day 4 of 100 Days of Code- Python


# Coin Flip Program
import random
# random.random() generates a float between 0.0000 and .9999999
rando = random.randint(0, 1)
if rando == 0:
    print("Tails")
else:
    print("Heads")


# Randomly picks who is buying lunch (random imported already on line 7)
names_string = input("Give me everybody's names, separated by a comma. ")
# .split() creates an array of the names, splitting into new index values after (", ")
names = names_string.split(", ")
length = len(names)
index = random.randint(0,length-1)
print(f"{names[index]} is going to buy the meal today!")


# Mark in an X in nested lists
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = 'X'

print(f"{row1}\n{row2}\n{row3}")


# Rock, Paper, Scissors game
# Random imported already on line 7
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

user_input = int(input("Let's play Roshambeaux! Enter 0 for rock, 1 for paper, or 2 for scissors."))
choices = [rock, paper, scissors]
computer_choice = random.randint(0,2)

print(f"You chose \n {choices[user_input]} \n The computer chose \n {choices[computer_choice]} \n")

# If user doesn't enter a valid input
if user_input > 2 or user_input < 0:
    print("You typed an invalid number, you lose!")

# User chose rock
if user_input == 0:
    if computer_choice == 0:
        print("It's a draw!")
    elif computer_choice == 1:
        print("You lost!")
    else:
        print("You won!")

# User chose paper
if user_input == 1:
    if computer_choice == 0:
        print("You won!")
    elif computer_choice == 1:
        print("It's a draw!")
    else:
        print("You lost!")

if user_input == 2:
    if computer_choice == 0:
        print("You lost!")
    elif computer_choice == 1:
        print("You won!")
    else:
        print("It's a draw!")

