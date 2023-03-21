from turtle import Turtle
import random

class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("purple")
    self.penup()
    self.shapesize(0.75, 0.75)
    self.speed("fastest")
    self.refresh()
  
  def refresh(self):
    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    self.setposition(x, y)