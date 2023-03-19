from turtle import Turtle, Screen

michael_angelo = Turtle()
screen = Screen()

def move_forwards():
    michael_angelo.forward(10)

def turn_left():
    michael_angelo.left(10)

def turn_right():
    michael_angelo.right(10)

def move_backwards():
    michael_angelo.backward(10)


def main():
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=turn_left)
    screen.onkey(key="d", fun=turn_right)
    screen.onkey(key="c", fun=screen.resetscreen)
    screen.exitonclick()

main()