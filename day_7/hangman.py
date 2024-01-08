from random import choice
from hangman_art import stages, logo
from hangman_words import word_list
from os import system, name

chosen_word = choice(word_list)
chosen_word_length = len(chosen_word)
display = []
lives = 6
end_of_game = False

def clear_screen():
  system('cls' if name == 'nt' else 'clear')

for _ in range(chosen_word_length):
    display += "_"

clear_screen()
print(logo)

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  clear_screen()

  if guess in display:
    print(f"You've already guessed {guess}, guess again.")

  for i in range(chosen_word_length):
    if chosen_word[i] == guess:
      display[i] = guess

  if guess in chosen_word:
    print(f"You guessed {guess}, that's in the word.")
  
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
      end_of_game = True
      print("You lose.")
      print(f"The word was {chosen_word}")

  print(stages[lives])
  print("".join(display))

  if "_" not in display:
    end_of_game = True
    print("You win!")