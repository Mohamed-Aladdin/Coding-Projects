from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.setposition(0, 270)
    self.hideturtle()
    self.update_score()

  def update_score(self):
    self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

  def clear(self):
    super().clear()
    self.score += 1
    self.update_score()

  def game_over(self):
    self.setposition(0, 0)
    self.write("GAME OVER!", False, ALIGNMENT, FONT)
