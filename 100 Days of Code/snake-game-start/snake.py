from turtle import Turtle

INITIAL_COUNT = 3
D = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.parts = []
        self.create()
        self.head = self.parts[0]

    def create(self):
        INITIAL_X = 0
        for _ in range(INITIAL_COUNT):
            part = Turtle(shape="square")
            part.color("white")
            part.penup()
            part.setposition(INITIAL_X, 0)
            INITIAL_X -= 20
            self.parts.append(part)

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            nx = self.parts[i-1].xcor()
            ny = self.parts[i-1].ycor()
            self.parts[i].setposition(nx, ny)
        self.head.forward(D)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)