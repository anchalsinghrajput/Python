from turtle import Screen, Turtle
import random as ran
t = Turtle()
t.speed("fastest")

colours = ["red", "orange", "green","pink","coral","blue","violet","black","cyan"]

t.pensize(0)

def draw_spiral(size_of_gap):
    for i in range (360//size_of_gap):
        t.color(ran.choice(colours))
        t.circle(100)
        t.setheading(t.heading()+size_of_gap)

draw_spiral(5)

s = Screen()
s.exitonclick()