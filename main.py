from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()

def move_forward():
    t.fd(5)

def move_backward():
    t.bk(5)

def turn_left():
    t.lt(5)

def turn_right():
    t.rt(5)

def reset_screen():
    t.reset()

s.onkey(move_forward, "Up")
s.onkey(move_backward, "Down")
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")
s.onkey(reset_screen, "c")


s.exitonclick()