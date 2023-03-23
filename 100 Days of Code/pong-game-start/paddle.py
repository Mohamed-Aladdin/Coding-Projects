from turtle import Turtle

class Paddle():

    def __init__(self):
        self.paddles = []
        self.positions = [(-390, 0), (380, 0)]
        self.create_paddle()

    def create_paddle(self):
        for position in self.positions:
            self.paddle = Turtle()
            self.paddle.penup()
            self.paddle.color("white")
            self.paddle.shape("square")
            self.paddle.shapesize(stretch_wid=4, stretch_len=1)
            self.paddle.setposition(position)
            self.paddles.append(self.paddle)

    def up_one(self):
        new_y = self.paddles[0].ycor() + 20
        if new_y > 260:
            pass
        else:
            self.paddles[0].setposition(self.paddles[0].xcor(), new_y)

    def down_one(self):
        new_y = self.paddles[0].ycor() - 20
        if new_y < -260:
            pass
        else:
            self.paddles[0].setposition(self.paddles[0].xcor(), new_y)

    def up_two(self):
        new_y = self.paddles[1].ycor() + 20
        if new_y > 260:
            pass
        else:
            self.paddles[1].setposition(self.paddles[1].xcor(), new_y)
    
    def down_two(self):
        new_y = self.paddles[1].ycor() - 20
        if new_y < -260:
            pass
        else:
            self.paddles[1].setposition(self.paddles[1].xcor(), new_y)

    def reset_paddles(self):
        self.paddles[0].setposition(self.positions[0])
        self.paddles[1].setposition(self.positions[1])