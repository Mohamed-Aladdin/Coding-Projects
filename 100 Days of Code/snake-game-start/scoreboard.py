from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.high_score = self.get_high_score()
    self.score = 0
    self.color("white")
    self.penup()
    self.hideturtle()
    self.update_score()

  def update_score(self):
    self.setposition(0, 270)
    self.write(f"Score: {self.score}. High Score: {self.high_score}", False, ALIGNMENT, FONT)

  def clear(self):
    super().clear()
    self.score += 1
    self.update_score()

  def game_over(self):
    if self.score > self.high_score:
      self.high_score = self.score
      self.set_high_score()
    self.score = 0
    self.setposition(0, 0)
    self.write("GAME OVER!", False, ALIGNMENT, FONT)

  def get_high_score(self):
    with open(r"Python\100 Days of Code\snake-game-start\data.txt") as data:
      high_score = int(data.read())
      return high_score
  
  def set_high_score(self):
    with open(r"Python\100 Days of Code\snake-game-start\data.txt", "w") as data:
      data.write(f"{self.high_score}")