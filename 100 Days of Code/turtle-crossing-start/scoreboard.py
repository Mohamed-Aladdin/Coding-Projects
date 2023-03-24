from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create()

    def create(self):
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setposition(-280, 260)
        self.write(f"Level: {self.level}", False, "left", FONT)

    def update(self):
        super().clear()
        self.level += 1
        self.create()

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over!\nMax level: {self.level}", False, "center", FONT)
