from random import choice
from hangman_art import stages, logo
from hangman_words import word_list
from os import system, name

MAX_LIVES = 6

def clear_screen():
  system('cls' if name == 'nt' else 'clear')

def initialize_game():
  chosen_word = choice(word_list)
  display = ["_" for _ in range(len(chosen_word))]
  guessed_letters = set()
  lives = MAX_LIVES
  return chosen_word, display, guessed_letters, lives

def process_guess(chosen_word: str, display: list, guess: str) -> bool:
  """Update the game state, and returns whether the user's guess was correct."""
  if guess in chosen_word:
    for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
        display[i] = guess
    print(f"You guessed {guess}, that's in the word.")
  else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    return False
  return True

def validate_guess(guessed_letters: set) -> str:
  """Returns a valid guess from the user."""
  guess = input("Guess a letter: ").lower()

  if not guess.isalpha() or len(guess) != 1:
    print("Please enter a single letter.")
  elif guess in guessed_letters:
    print(f"You've already guessed {guess}, guess again.")
  else:
    return guess

def check_game_over(chosen_word: str, display: list, lives: int) -> bool:
  """Returns True if game is over, False otherwise."""
  if "_" not in display:
    print("You win!")
    return True
  if lives == 0:
    print("You lose.")
    print(f"The word was {chosen_word}")
    return True
  return False

def main():
  chosen_word, display, guessed_letters, lives = initialize_game()
  clear_screen()
  print(logo)

  while True:
    guess = validate_guess(guessed_letters)
    if guess is not None:
      guessed_letters.add(guess)
      clear_screen()

      if not process_guess(chosen_word, display, guess):
        lives -= 1

      print(stages[lives])
      print("".join(display))
      print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")

    if check_game_over(chosen_word, display, lives):
      break

"""Runs if file is run directly, not if imported."""
if __name__ == "__main__":
  main()