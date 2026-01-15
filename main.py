from turtle import Turtle, Screen

t = Turtle()
s = Screen()
s.listen()

def move_up():
    # set to north
    t.setheading(90)
    t.fd(20)

def move_down():
    # set to south
    t.setheading(270)
    t.fd(20)

def move_right():
    # set to east
    t.setheading(0)
    t.fd(20)

def move_left():
    # set to west
    t.setheading(180)
    t.fd(20)

s.onkey(move_up, "Up")
s.onkey(move_down, "Down")
s.onkey(move_right, "Right")
s.onkey(move_left, "Left")


s.exitonclick()