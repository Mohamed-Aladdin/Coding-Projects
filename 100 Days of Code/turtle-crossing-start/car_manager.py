from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    
    def __init__(self):
        self.cars = []
        self.velocity = STARTING_MOVE_DISTANCE

    def create(self):
        n = random.randint(1, 6)
        if n == 1:
            self.car = Turtle("square")
            self.car.penup()
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.color(random.choice(COLORS))
            self.car.setposition(300, random.randint(-240, 240))
            self.cars.append(self.car)
    
    def move(self):
        for car in self.cars:
            car.backward(self.velocity)
            if car.xcor() < -350:
                car.clear()
                self.cars.remove(car)

    def level_up(self):
        self.velocity += MOVE_INCREMENT