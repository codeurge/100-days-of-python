print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\". ").lower()

if direction == "left":
  print("You come to a lake. There is an island in the middle of the lake.")
  swim_or_wait = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").lower()
  if swim_or_wait == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    door = input("One red, one yellow, and one blue. Which color do you choose? ").lower()
    if door == "yellow":
      print("You found the treasure! You Win!")
    elif door == "red":
      print("It's a room full of fire. Game Over.")
    elif door == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
  exit()
