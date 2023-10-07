import turtle

#---------------------------#
screen = turtle.Screen()
width = 1920
height = 720
screen.bgcolor("black")
screen.setup(width, height)
#---------------------------#

#---------------------------#
left_border_coordinate = -380
right_border_coordinate = 380
upper_border_coordinate = 300
bottom_border_coordinate = -300

brush = turtle.Turtle()
brush.color("white")
brush.width(2)
brush.speed(0)
brush.penup()
brush.goto(right_border_coordinate, upper_border_coordinate)
brush.pendown()
brush.left(180)
brush.goto(left_border_coordinate, upper_border_coordinate)
brush.left(90)
brush.goto(left_border_coordinate, bottom_border_coordinate)
brush.left(90)
brush.goto(right_border_coordinate, bottom_border_coordinate)
brush.left(90)
brush.goto(right_border_coordinate, upper_border_coordinate)
brush.hideturtle()
#---------------------------#

#---------------------------#
score1 = 0
score2 = 0

score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, upper_border_coordinate + 10)
score.write("Player1: 0   Player2: 0", align="center", font=("Courier", 24, "normal"))

#---------------------------#

#---------------------------#
player_step = 15

player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(5,1)
player1.penup()
player1.goto(-350, 0)

player1_length = 60
player1_width = 20

player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(5,1)
player2.penup()
player2.goto(350, 0)

player2_length = 60
player2_width = 20

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(1,1)
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

ball_radius = 15
#---------------------------#

#---------------------------#
def player1_up():
    if player1.ycor() + player1_length < upper_border_coordinate:
        player1.sety(player1.ycor() + player_step)

def player1_down():
    if player1.ycor() - player1_length > bottom_border_coordinate:
        player1.sety(player1.ycor() - player_step)

def player2_up():
    if player2.ycor() + player2_length < upper_border_coordinate:
        player2.sety(player2.ycor() + player_step)

def player2_down():
    if player2.ycor() - player2_length > bottom_border_coordinate:
        player2.sety(player2.ycor() - player_step)

screen.listen()
screen.onkey(player1_up, "w")
screen.onkey(player1_down, "s")
screen.onkey(player2_up, "Up")
screen.onkey(player2_down, "Down")
#---------------------------#
is_play = True

while is_play:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() + ball_radius > upper_border_coordinate or ball.ycor() - ball_radius < bottom_border_coordinate:
        ball.dy *= -1

    if ball.xcor() - ball_radius < left_border_coordinate:
        score2 += 1
        score.clear()
        score.write("Player1: {} Player2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()
    elif ball.xcor() + ball_radius > right_border_coordinate:
        score1 += 1
        score.clear()
        score.write("Player1: {} Player2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.hideturtle()
        ball.goto(0,0)
        ball.showturtle()

    if ball.xcor() <= player1.xcor() + player1_width and ball.ycor() < player1.ycor() + player1_length and ball.ycor() > player1.ycor() - player1_length:
        ball.dx *= -1
    elif ball.xcor() >= player2.xcor() - player2_width and ball.ycor() < player2.ycor() + player2_length and ball.ycor() > player2.ycor() - player2_length:
        ball.dx *= -1

    if score1 == 5:
        is_play = False
        score.clear()
        score.write("Player 1 won!", align="center", font=("Courier", 24, "normal"))
    elif score2 == 5:
        is_play = False
        score.clear()
        score.write("Player2 won!", align="center", font=("Courier", 24, "normal"))

turtle.done()