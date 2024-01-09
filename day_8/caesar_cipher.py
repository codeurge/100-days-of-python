from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
  print(logo)

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "decode":
      shift *= -1
    for letter in text:
      # Preserve special characters, spaces, and punctuation.
      if letter not in alphabet:
        cipher_text += letter
      else:
        position = alphabet.index(letter)
        # This automatically wraps around the alphabet array.
        new_position = (position + shift) % 26
        cipher_text += alphabet[new_position]
    return cipher_text

  print(f"The {direction}d text is {caesar(text=text, shift=shift, direction=direction)}")
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "yes":
    main()

"""Runs if file is run directly, not if imported."""
if __name__ == "__main__":
  main()
