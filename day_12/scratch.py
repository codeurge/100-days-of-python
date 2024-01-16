enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")
  
increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# print(potion_strength)

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

# There is no block scope
if 3 > 2:
  a_variable = 10 # This variable is available outside the if block

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
  new_enemy = enemies[0]

# Modifying Global Scope

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants
PI = 3.14159
TWITTER_HANDLE = "@codeurge"

def calc():
  print(PI)
