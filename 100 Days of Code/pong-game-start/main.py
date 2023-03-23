from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("P O N G!")
screen.tracer(0)

initial_y = -270
for i in range(19):
    splitter = Turtle()
    splitter.penup()
    splitter.shape("square")
    splitter.color("white")
    splitter.shapesize(stretch_len=0.3)
    splitter.setposition(0, initial_y)
    initial_y += 30

paddle = Paddle()
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkey(paddle.up_one, "w")
screen.onkey(paddle.up_two, "Up")
screen.onkey(paddle.down_one, "s")
screen.onkey(paddle.down_two, "Down")

end_game = False
while not end_game:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce_y()
    
    if (ball.distance(paddle.paddles[0]) <= 50 and ball.xcor() <= -360) or (ball.distance(paddle.paddles[1]) <= 50 and ball.xcor() >= 360):
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.clear_score(1)
        ball.reset_ball()
        paddle.reset_paddles()
    elif ball.xcor() < -400:
        scoreboard.clear_score(2)
        ball.reset_ball()
        paddle.reset_paddles()

    if scoreboard.score_one == 10 or scoreboard.score_two == 10:
        scoreboard.game_over()
        end_game = True

screen.exitonclick()