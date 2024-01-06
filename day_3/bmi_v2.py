height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / height ** 2

if bmi < 18.5:
    interpretation = "you are underweight"
elif bmi < 25:
    interpretation = "you have a normal weight"
elif bmi < 30:
    interpretation = "you are slightly overweight"
elif bmi < 35:
    interpretation = "you are obese"
elif bmi >= 35:
    interpretation = "you are clinically obese"

print(f"Your BMI is {bmi}, {interpretation}.")