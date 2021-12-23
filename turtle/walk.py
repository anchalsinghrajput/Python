import random
import turtle

t = turtle.Turtle()
t.pensize(15)
t.speed(0)

# colours = ["red", "orange", "green","pink","coral","blue","violet","black","cyan"]
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

directions = [0,90,180,270]

for i in range (200):
    t.forward(30)
    # t.color(random.choice(colours))
    t.color(random_color())
    t.setheading(random.choice(directions))


s = turtle._Screen()
s.exitonclick()