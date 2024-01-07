student_scores = input().split()
high_score = 0

for student_score in student_scores:
  student_score = int(student_score)
  if student_score > high_score:
    high_score = student_score

print(f"The highest score in the class is: {high_score}")