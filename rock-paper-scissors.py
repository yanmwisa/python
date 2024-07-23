import random
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
game_images = [ rock , paper  , scissors]

#Write your code below this line 👇import random

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

game_images = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input("What is your choice? : "))
computer_choice = random.randint(0, 2)

print("You chose:")
print(game_images[user_choice])
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0:  # Rock
    if computer_choice == 2:  # Scissors
        print("You won!")
    elif computer_choice == 1:  # Paper
        print("You lose, computer won!")
    else:
        print("It's a tie!")
elif user_choice == 1:  # Paper
    if computer_choice == 0:  # Rock
        print("You won!")
    elif computer_choice == 2:  # Scissors
        print("You lose, computer won!")
    else:
        print("It's a tie!")
elif user_choice == 2:  # Scissors
    if computer_choice == 1:  # Paper
        print("You won!")
    elif computer_choice == 0:  # Rock
        print("You lose, computer won!")
    else:
        print("It's a tie!")









