from turtle import Screen, Turtle
from typing import Sized
import random   

t = Turtle()
t.pensize(6)

def shape(side):
    angle = 360/side
    for i in range(side):
        t.forward(100)
        t.right(angle)

colours = ["red", "orange", "green","pink","coral","blue","violet","black","cyan"]
for side in range (3,11):
    t.color(random.choice(colours))
    shape(side)

s = Screen()
s.exitonclick()