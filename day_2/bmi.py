height = input("What is your height in m? ")
weight = input("What is your weight in kg? ")

bmi = int(weight) / float(height) ** 2  # ** is the exponent operator
print("Your BMI is:", int(bmi))