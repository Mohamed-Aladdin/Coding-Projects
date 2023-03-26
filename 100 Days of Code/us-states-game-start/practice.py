import pandas

# data = pandas.read_csv(r"Python\100 Days of Code\us-states-game-start\50_states.csv")
# print(data["state"])

# data = pandas.read_csv(r"Python\100 Days of Code\us-states-game-start\weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# print(sum(data_list) / len(data_list))

# print(data[data.temp == data.temp.max()])

# student_dict = {
#   "students": ["Amy", "James", "Angela"],
#   "scores": [76, 56, 65]
# }
# students_data = pandas.DataFrame(student_dict)
# print(students_data)
# students_data.to_csv(r"Python\100 Days of Code\us-states-game-start\students_scores.csv")

data = pandas.read_csv(r"Python\100 Days of Code\us-states-game-start\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
  "Fur Color": ["Gray", "Cinnamon", "Black"],
  "Count": [gray, cinnamon, black]
}

color_data = pandas.DataFrame(color_dict)
color_data.to_csv(r"Python\100 Days of Code\us-states-game-start\squirrel_count.csv")