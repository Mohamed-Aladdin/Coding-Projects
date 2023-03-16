def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def left_is_clear():
    turn_around()
    if right_is_clear():
        turn_around()
        return True
    else:
        turn_around()
        return False
        

def escape():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
                
escape()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
