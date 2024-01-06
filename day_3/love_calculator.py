print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

combined_names = name1.lower() + name2.lower()
true = 0
love = 0

true += combined_names.count('t')
true += combined_names.count('r')
true += combined_names.count('u')
true += combined_names.count('e')

love += combined_names.count('l')
love += combined_names.count('o')
love += combined_names.count('v')
love += combined_names.count('e')

score = int(f"{true}{love}")

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")