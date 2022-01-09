 #  (turtle is a graphical library, 
 #  which means you'll need to create a separate window (called the screen) to carry out each drawing command.
 #  You can create this screen by initializing a variable for it.
 #  In Python, you use variables to store information that you'll use later on in your program)

import turtle;

wn = turtle.Screen()                                     #creating window screen 
wn.title("Pong by Anchal Singh")
wn.bgcolor("pink")                                       #background colour of the window
wn.setup(width=900, height=700)                           #window size in pixel
wn.tracer(0)                                              #speed up the game processing

#scores
score_a=0
score_b=0


# paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)                                        #set up the speed to the max
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)          #stretching the paddle size 
paddle_a.penup()
paddle_a.goto(-430,0)

# paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)                                        #set up the speed to the max
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)          #stretching the paddle size 
paddle_b.penup()
paddle_b.goto(+430,0)

# ball
ball = turtle.Turtle()
ball.speed(0)                                        #set up the speed to the max
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)                                       #setting ball at the middle of the window
ball.dx = 2                                          # moving the ball to the right by 2 px
ball.dy = -2                                          # moving the ball to the up by 2 px

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player A : 0  Player B : 0",align="center",font=("Courtier",24,"normal"))   #defoult score on the screen 


#function for moving the paddle1 up
def paddle_a_up() :                                    
    y=paddle_a.ycor()                               #paddle a is the name of the object
    y+=20
    paddle_a.sety(y)

#function for moving the paddle1 down
def paddle_a_down() :                                    
    y=paddle_a.ycor()                               
    y-=20
    paddle_a.sety(y)

#function for moving the paddle2 up
def paddle_b_up() :                                    
    y=paddle_b.ycor()                               
    y+=20
    paddle_b.sety(y)

#function for moving the paddle2 down
def paddle_b_down() :                                    
    y=paddle_b.ycor()                               
    y-=20
    paddle_b.sety(y)

#setting the key for moving paddle up and down
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#game loop
while True:
    wn.update()                                          #updates the Screen whenever game starts from beginning 
    
    #move the ball 
    ball.setx(ball.xcor()+ball.dx/4)                    #speed of the ball is decreased by 4
    ball.sety(ball.ycor()+ball.dy/4)

    #border checking
    if ball.ycor()>340:
        ball.sety(340)
        ball.dy *=-1
       

    if ball.ycor()<-340:
        ball.sety(-340)
        ball.dy *=-1

    if ball.xcor()>440:
        ball.goto(0,0)
        ball.dx *=-1
        score_a+=1      #if the ball goes off right side of the screen player A gets a point
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b),align="center",font=("Courtier",24,"normal"))  #updating the scores

    if ball.xcor()<-440:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1      #if the ball goes off left  side of the screen player A gets a point
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b),align="center",font=("Courtier",24,"normal"))  #updating the score

    # when paddle2 (right side padlle) and ball collides
    if (ball.xcor()>400 and ball.xcor()<410) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(400)
        ball.dx *= -1

    # when paddle1 (left side padlle) and ball collides
    if (ball.xcor()<-400 and ball.xcor()>-410) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-400)
        ball.dx *= -1

