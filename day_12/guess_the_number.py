import random

def get_difficulty():
  while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty in ["easy", "hard"]:
      return difficulty
    print("Invalid difficulty. Please enter 'easy' or 'hard'.")

def get_guess():
  return int(input("Make a guess: "))

def play_game():
  number = random.randint(1, 100)
  attempts = 10 if get_difficulty() == "easy" else 5

  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = get_guess()

    if guess == number:
      print(f"You got it! The answer was {number}.")
      return
    elif guess > number:
      print("Too high.")
    else:
      print("Too low.")
    attempts -= 1

  print("You've run out of guesses, you lose.")

play_game()