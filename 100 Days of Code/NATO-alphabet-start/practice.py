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

#Exception Handling

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)