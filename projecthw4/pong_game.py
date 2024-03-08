import turtle as t
import os

player_a_score = 0
player_b_score = 0

window = t.Screen()
window.title("The Pong Game")
window.bgcolor("tan")
window.setup(width=900, height=650)
window.tracer(0)

leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("navy")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-400, 0)

rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("navy")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(400, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.2
ballydirection = 0.2

pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("Player A: 0             Player B: 0", align="center", font=('Aptos Display', 26, 'normal'))

pe = t.Turtle()
pe.color("black")
pe.penup()
pe.hideturtle()
pe.goto(0,-300)
pe.write("Mohamed Ladgham", align="left", font=('Brush Script MT', 20, 'bold'))

def leftpaddleup():
    y = leftpaddle.ycor()
    y += 20
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 20
    leftpaddle.sety(y)

def rightpaddleup():
    y = rightpaddle.ycor()
    y += 20
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 20
    rightpaddle.sety(y)

window.listen()
window.onkeypress(leftpaddleup, 'z')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)
    # border set up
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}           Player B: {}".format(player_a_score, player_b_score), align="center", font=('Monaco', 28, "normal"))
        os.system("afplay wallhit.wav&")
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}           Player B: {}".format(player_a_score, player_b_score), align="center", font=('Monaco', 28, "bold"))
        os.system("afplay wallhit.wav&")
    # handling the collisions with paddles
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
        os.system("afplay paddle.wav&")
