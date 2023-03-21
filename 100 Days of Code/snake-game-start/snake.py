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
        initial_x = 0
        for _ in range(INITIAL_COUNT):
            self.add_part(initial_x)
            initial_x -= 20

    def add_part(self, x):
        part = Turtle(shape="square")
        part.color("white")
        part.penup()
        part.setposition(x, 0)
        self.parts.append(part)

    def extend(self):
        self.add_part(self.parts[-1].xcor())

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