import random
import pandas

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Angela"
new_name = [char for char in name]
print(new_name)

double_range = [n*2 for n in range(1, 5)]
print(double_range)

names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
new_names = [name.upper() for name in names if len(name) > 5]
print(new_names)

students = {student:random.randint(1, 100) for student in names}
print(students)

passed_students = {student:score for student, score in students.items() if score >= 60}
print(passed_students)

students_dict = {
  "student": ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"],
  "score": [20, 6, 45, 52, 46, 47]
}

students_df = pandas.DataFrame(students_dict)
print (students_df)

for index, row in students_df.iterrows():
  print(row.score)

peeps = {row.student:row.score for index, row in students_df.iterrows()}
print(peeps)