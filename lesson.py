from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

segments = []
start_pos = [(0, 0), (-20, 0), (-40, 0)]
for pos in start_pos:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)

screen.update()
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()
