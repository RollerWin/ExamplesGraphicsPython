import turtle
import random
import time


screen = turtle.Screen()
width=1280
height=720
screen.setup(width, height)

t = turtle.Turtle()
t.speed(0) 
turtle.tracer(1, None)

screen.bgcolor("black")

# Функция для рисования звезд
def draw_star():
    t.penup()
    x = random.randint(-640, 640)
    y = random.randint(-360, 360)
    t.goto(x, y)
    t.pendown()
    size = random.randint(2, 5)

    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.penup()
    
num_stars = random.randint(50, 100)

for _ in range(num_stars):
    t.color("white")
    draw_star()

moon = turtle.Turtle()
moon.shape("circle")
moon.color("white")
moon.turtlesize(6)
moon.penup()
moon.speed(0)

shade = turtle.Turtle()
shade.shape("circle")
shade.color("black")
shade.turtlesize(6)
shade.penup()
shade.speed(0)

default_moon_x = -580
default_moon_y = -280

default_shade_x = default_moon_x + 120
default_shade_y = default_moon_y

shade_x = default_shade_x
shade_y = default_shade_y

moon_x = default_moon_x
moon_y = default_moon_y

coefficient = 1201
step = 10

while True:
    moon.goto(moon_x, moon_y)
    shade.goto(shade_x, shade_y)

    moon_x += step
    moon_y = -1 * (moon_x ** 2) / coefficient 

    shade_x += step - 2
    shade_y = moon_y

    if moon_x == width / 2:
        moon_x = default_moon_x
        shade_x = default_shade_x

    screen.update()
    time.sleep(0.1)  # Подождите некоторое время