from turtle import Turtle, Screen
import random

leonardo = Turtle()
donatello = Turtle()
rafaello = Turtle()
michael_angelo = Turtle()

screen = Screen()
screen.setup(600, 600, -300, 0)
colors = ["blue", "purple", "red", "orange"]
paces = [2, 4, 6, 8, 10]
screen.title("Welcome to the most fun turtle race!")
turtles = screen.turtles()

def get_guess():
  guess = screen.textinput("Hey there!", "What's the color of the winning turtle?").lower()
  return guess

def ready_steady():
  y = -100
  i = 0
  for turtle in turtles:
    turtle.shape("turtle")
    turtle.pencolor("white")
    turtle.color(colors[i])
    turtle.penup()
    turtle.setposition(-290, y)
    y += 50
    i += 1

def go():
  x = -290
  while x < 280:
    for turtle in turtles:
      turtle.forward(random.choice(paces))
      if turtle.xcor() >= 280:
        print(f"{turtle.fillcolor()} made it first!")
        return turtle.fillcolor()

def is_winner(guess, func):
  return guess == func

def main():
  end_game = False
  while not end_game:
    guess = get_guess()
    if guess not in colors:
      print("Please pick a valid color!")
      continue
    ready_steady()
    if is_winner(guess, go()):
      print("Congrats, You've won!")
    else:
      print("You've lost!")
    replay = input("Would you like to go again? press enter to replay (q to quit): ")
    if replay == "q":
      screen.bye()
      end_game = True
    else:
      screen.resetscreen()
      continue

main()