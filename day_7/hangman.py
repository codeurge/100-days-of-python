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

"""Returns True if life is lost, False otherwise."""
def handle_guess(chosen_word, display, guessed_letters):
  guess = input("Guess a letter: ").lower()
  clear_screen()

  if not guess.isalpha() or len(guess) != 1:
    print("Please enter a single letter.")
  elif guess in guessed_letters:
    print(f"You've already guessed {guess}, guess again.")
  elif guess in chosen_word:
    for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
        display[i] = guess
    guessed_letters.add(guess)
    print(f"You guessed {guess}, that's in the word.")
  else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    guessed_letters.add(guess)
    return True
  return False

"""Returns True if game is over, False otherwise."""
def check_game_over(display, lives, chosen_word):
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
    if handle_guess(chosen_word, display, guessed_letters):
      lives -= 1

    print(stages[lives])
    print("".join(display))
    print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")

    if check_game_over(display, lives, chosen_word):
      break

"""Runs if file is run directly, not if imported."""
if __name__ == "__main__":
  main()