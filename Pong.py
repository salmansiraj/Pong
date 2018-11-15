import turtle


window = turtle.Screen()
window.title("Pong Game (Salman Siraj)")
window.bgcolor("black")
window.setup(width = 800, height = 600)

window.tracer(0) # No changing orientation of screen


# Player 1 
player1 = turtle.Turtle() # turtle object 
# print(type(player1))
player1.speed(0)
player1.shape("square")
player1.color("light gray")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.penup()
player1.goto(-350, 0) # left side of screen

def moveUpOne(): 
    yCord = player1.ycor()
    yCord += 20
    player1.sety(yCord)

def moveDownOne():
    yCord = player1.ycor()
    yCord -= 20
    player1.sety(yCord)
    

# Player 2 
player2 = turtle.Turtle()  # turtle object
player2.speed(0)
player2.shape("square")
player2.color("light gray")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.penup()
player2.goto(350, 0)  # right side of screen

def moveUpTwo():
    yCord = player2.ycor()
    yCord += 20
    player2.sety(yCord)

def moveDownTwo():
    yCord = player2.ycor()
    yCord -= 20
    player2.sety(yCord)


# Ball 
ball = turtle.Turtle()  # turtle object
ball.speed(0)
ball.shape("circle")
ball.color("blue")
# ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0, 0)  # right side ofball
ball.changeX = 2
ball.changeY = 2


# Initualized player scores 
scoreplayerOne = 0 
scoreplayerTwo = 0 


# Function Keys for Players
window.listen()
window.onkeypress(moveUpOne, "w")
window.onkeypress(moveDownOne, "s")
window.onkeypress(moveUpTwo, "Up")
window.onkeypress(moveDownTwo, "Down")


# Scoreboard
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player 1: 0 player 2: 0", align="center", font=("Courier", 24, "normal"))




# Gameplay
while True: 
    window.update() 
    # move ball 
    ball.setx(ball.xcor() + ball.changeX)
    ball.sety(ball.ycor() + ball.changeY)

    # Border case 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.changeY *= -1 # Reflect direction of ball

    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.changeY *= -1  # Reflect direction of ball

    if ball.xcor() > 390:
        ball.setx(0) # out of x scope, return to center
        ball.changeX *= -1  # Reflect direction of ball
        scoreplayerOne += 1
        pen.clear()
        pen.write("player 1: " + str(scoreplayerOne) + " player 2: " +
                str(scoreplayerTwo), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.changeX *= -1  # Reflect direction of ball
        scoreplayerTwo += 1
        pen.clear()
        pen.write("player 1: " + str(scoreplayerOne) + " player 2: " +
                str(scoreplayerTwo), align="center", font=("Courier", 24, "normal"))

    if ((ball.xcor() > 340 and ball.xcor() < 350) and ( ball.ycor() < player2.ycor() + 40 
                            and ball.ycor() > player2.ycor() - 40)):
        ball.setx(340)
        ball.changeX *= -1 # reflect off player

    if ((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40
                                and ball.ycor() > player1.ycor() - 40)):
        ball.setx(-340)
        ball.changeX *= -1  # reflect off player
