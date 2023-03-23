from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create()
        self.xpos = 12
        self.ypos = 11
        self.move_speed = 0.1

    def create(self):
        self.penup()
        self.color("white")
        self.shape("circle")
    
    def move(self):
        new_x = self.xcor() + self.xpos
        new_y = self.ycor() + self.ypos
        self.setposition(new_x, new_y)

    def bounce_y(self):
        self.ypos *= -1
    
    def bounce_x(self):
        self.xpos *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.home()
        self.xpos *= -1
        self.ypos *= -1
        self.move_speed = 0.1