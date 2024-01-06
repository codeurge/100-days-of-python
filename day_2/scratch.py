# Data Types

# String
"Hello"
print("Hello"[4])

# Integer
123
print(123 + 345)

print(60_000_000)

# Float
3.14159
print(3.14159)

# Boolean
True
False

# Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print(num_char, type(num_char))
print(new_num_char, type(new_num_char))
# The following would fail because num_char is an integer and cannot be concatenated with a string.
# print("Your name has " + num_char + " characters.")
print("Your name has " + new_num_char + " characters.")

# Mathematical Operations in Python
3 + 5 # Addition
7 - 4 # Subtraction
3 * 2 # Multiplication
print(type(6 / 3)) # Division will always return a float
2 ** 3 # 2 to the power of 3

print(3 * 3 + 3 / 3 - 3) # PEMDAS
print(3 * (3 + 3) / 3 - 3)  

# Number Manipulation and F Strings in Python
score = 0
height = 1.8
isWinning = True
# f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
