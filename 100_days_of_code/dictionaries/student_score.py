student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}


for student in student_scores:
  score = student_scores[student]
  if score >= 91 and score <= 100:
    student_grades[score] = "Outstanding"
  elif score >= 81 and score <= 90:
    student_grades[score] = "Exceeds Expectations"
  elif score >= 71 and score <= 80:
    student_grades[score] = "Acceptable"
  elif score <= 70:
    student_grades[score] = "Fail"
    

print(student_grades)