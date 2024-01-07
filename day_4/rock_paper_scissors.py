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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu_choice = random.randint(0, 2)

choices = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print("You chose:")
  print(choices[user_choice])

  print("Computer chose:")
  print(choices[cpu_choice])

  if user_choice == 0 and cpu_choice == 2:
    print("You win!")
  elif cpu_choice == 0 and user_choice == 2:
    print("You lose!")
  elif cpu_choice > user_choice:
    print("You lose!")
  elif user_choice > cpu_choice:
    print("You win!")
  elif cpu_choice == user_choice:
    print("It's a draw!")

