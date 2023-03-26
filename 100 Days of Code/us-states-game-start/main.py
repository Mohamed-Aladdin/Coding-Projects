import turtle
import pandas

data = pandas.read_csv(r"Python\100 Days of Code\us-states-game-start\50_states.csv")

image = r"Python\100 Days of Code\us-states-game-start\blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic(image)
screen.setup(700, 500)

def get_coordinates(guess):
  x = int(data[data.state == guess].x)
  y = int(data[data.state == guess].y)
  return x , y

def generate_states(found, states):
  for state in states:
    if state in found:
      states.remove(state)
  missing_states = pandas.DataFrame(states)
  missing_states.to_csv(r"Python\100 Days of Code\us-states-game-start\missing_states.csv")

def main():
  end_game = False
  score = 0
  found = []
  states = data.state.tolist()
  while not end_game:
    guess = screen.textinput(f"{score}/50 States Correct", "Enter a state's name").title()

    if guess in data.state.unique() and guess not in found:
      score += 1
      found.append(guess)
      x, y = get_coordinates(guess)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      t.setposition(x, y)
      t.write(f"{guess}", False, "center")
    elif guess == "Exit":
      generate_states(found, states)
      end_game = True

    if len(found) == 50:
      end_game = True

main()