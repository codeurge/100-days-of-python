import random

names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")

random_number = random.randint(0, len(names) - 1)
person = names[random_number]

print(f"{person} is going to buy the meal today!")