###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
import turtle
from turtle import Turtle, Screen
import random
import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)

## x = 300, y = 250
michael_angelo = Turtle()
michael_angelo.shape("turtle")
michael_angelo.color("green")
michael_angelo.speed("fastest")
turtle.colormode(255)

## Challenge No.1:

# i = 0
# while i < 4:
#     print(michael_angelo.pos())
#     michael_angelo.forward(100)
#     michael_angelo.left(90)
#     i += 1

## Challenge No.2:

# i = 0
# while i < 300:
#     michael_angelo.pendown()
#     michael_angelo.forward(5)
#     michael_angelo.penup()
#     michael_angelo.forward(5)
#     i += 10

## Challenge No.3:

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        michael_angelo.forward(100)
        michael_angelo.left(angle)

clrs = ["aquamarine", "orange red", "magenta", "chartreuse", "blue", "yellow", "saddle brown", "dark slate blue", "violet", "crimson"]

# for n in range(3, 11):
#     michael_angelo.color(random.choice(clrs))
#     draw_shape(n)

## Challenge No.4:

def random_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    colour = (r, g, b)
    return colour

def fancy_move():
    michael_angelo.setheading(random.choice([0, 90, 180, 270]))
    michael_angelo.pencolor(random_color())
    michael_angelo.forward(25)

# for i in range(200):
#     fancy_move()

## Challenge No.5:

def draw_spirograph():
    michael_angelo.pencolor(random_color())
    michael_angelo.circle(100)

# i = 0
# while i < 360:
#     draw_spirograph()
#     michael_angelo.setheading(i)
#     i += 5

## Final Project:

def color_from_image():
    img = colorgram.extract('image.jpg', 35)
    colors = []
    for i in range(35):
        r = img[i].rgb.r
        g = img[i].rgb.g
        b = img[i].rgb.b
        tup = (r, g, b)
        colors.append(tup)
    return colors

def move(d):
    michael_angelo.dot(d, random.choice(color_from_image()))
    michael_angelo.forward(2.5*d)

screen = Screen()
screen.screensize(600, 600)
michael_angelo.penup()
michael_angelo.hideturtle()
y = -300
while y < 300:
    x = -300
    michael_angelo.setpos(x, y)
    while x < 300:
        move(20)
        x += 50
    y += 50
screen.exitonclick()