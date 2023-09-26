import turtle
import random

def drawbar(height, color):
    brush.fillcolor(color)
    
    brush.begin_fill()
    brush.left(90)
    brush.forward(height)
    brush.write(str(height))
    brush.right(90)
    brush.forward(20)
    brush.right(90)
    brush.forward(height)
    brush.left(90)
    brush.end_fill()

default_price = 300
max_value = 500
min_value = 20
number_of_values = 25

values = [0] * number_of_values

for i in range(number_of_values):
    values[i] = random.randint(min_value, max_value)

border_length = 10
maxheight = max(values)
numbers = len(values)
good_price_color = "green"
bad_price_color = "red"

screen = turtle.Screen()
screen.setworldcoordinates(0 - border_length, 0 - border_length, 40 * numbers + border_length, maxheight+border_length)
brush = turtle.Turtle()

for i in range(numbers):
    if values[i] >= default_price:
        drawbar(values[i], good_price_color)
    else:
        drawbar(values[i], bad_price_color)

screen.exitonclick()