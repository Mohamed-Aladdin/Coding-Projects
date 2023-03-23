from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "bold")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score_one = 0
        self.score_two = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score(1)
        self.update_score(2)

    def update_score(self, p):
        if p == 1:
            self.setposition(-150, 230)
            self.write(f"Player {p}\n    {self.score_one}", False, ALIGNMENT, FONT)
        else:
            self.setposition(150, 230)
            self.write(f"Player {p}\n    {self.score_two}", False, ALIGNMENT, FONT)

    def clear_score(self, p):
        super().clear()
        if p == 1:
            self.score_one += 1
        else:
            self.score_two += 1
        self.update_score(1)
        self.update_score(2)

    def game_over(self):
        if self.score_one > self.score_two:
            self.setposition(200, 0)
            self.write(f"Game Over! Player 1 wins.", False, ALIGNMENT, ("Courier", 16, "bold"))
        else:
            self.setposition(-200, 0)
            self.write(f"Game Over! Player 1 wins.", False, ALIGNMENT, ("Courier", 16, "bold"))