import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()

screen.setup(600, 600)
screen.listen()
screen.onkey(player.move, "w")

end_game = False
while not end_game:
    screen.update()
    time.sleep(0.1)

    car_manager.create()
    car_manager.move()

    for car in car_manager.cars:
        if player.distance(car) <= 20:
            scoreboard.game_over()
            end_game = True

    if player.ycor() >= 280:
        scoreboard.update()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()