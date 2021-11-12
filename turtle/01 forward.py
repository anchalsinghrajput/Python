from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

myScreen = Screen()
print(myScreen.canvheight)          # canvheight() is the height of the turtle screen
print(myScreen.canvwidth)
myScreen.exitonclick()              # exitonclick() is used to show the turtle screen till we click onto he screen
