from turtle import *
speed(100)
tracer(0)
k = 18
for i in range(2):
    forward(75*k)
    right(270)
    forward(80*k)
    right(270)
pu()
backward(13*k)
right(90)
backward(17*k)
left(90)
pd()
for i in range(2):
    forward(63*k)
    right(90)
    forward(57*k)
    right(90)
pu()
for x in range(-60,60):
    for y in range(-60,60):
        goto(x*k,y*k)
        dot()
exitonclick()
