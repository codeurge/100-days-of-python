student_heights = input("Input a list of student heights ").split()
num_of_students = 0
total_height = 0

for student_height in student_heights:
  num_of_students += 1
  total_height += int(student_height)

print(f"total height = {total_height}")
print(f"number of students = {num_of_students}")
print(f"average height = {round(total_height / num_of_students)}")