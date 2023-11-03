import turtle
import random
import math

#---------------------------#
default_price = 300
max_value = default_price + 20
min_value = default_price - 20
current_price = random.randint(min_value, max_value)
epsilon = 20
step = 15
is_up = 0

left_x_coordinate = -400
left_y_coordinate = -400

right_x_coordinate = 400
right_y_coordinate = 400

x_length = abs(left_x_coordinate) + right_x_coordinate
y_length = abs(left_y_coordinate) + right_y_coordinate

good_price_color = "green"
bad_price_color = "red"

screen = turtle.Screen()
screen.setworldcoordinates(left_x_coordinate, left_y_coordinate, right_x_coordinate, right_y_coordinate)
width = x_length + 300
height = y_length - 50
screen.setup(width, height)
brush = turtle.Turtle()
#---------------------------#

brush.speed(0)

brush.penup()
brush.goto(left_x_coordinate, left_y_coordinate)
brush.pendown()

brush.forward(x_length)

brush.penup()
brush.goto(left_x_coordinate, left_y_coordinate)
brush.pendown()

brush.left(90)
brush.forward(y_length)

brush.penup()
brush.goto(left_x_coordinate - 100, 0)
brush.write("Стоимость")

brush.goto(0, left_y_coordinate - 25)
brush.write("Время")

brush.goto(left_x_coordinate, left_y_coordinate)
brush.pendown()

for i in range(0, y_length + 1, 50):
    brush.setheading(90)
    brush.penup()
    brush.goto(left_x_coordinate, i + left_y_coordinate)
    brush.pendown()

    brush.right(90)
    brush.forward(5)
    brush.left(180)
    brush.forward(10)

    brush.penup()
    brush.goto(left_x_coordinate - 30, i + left_y_coordinate)
    brush.write(str(i))
    brush.pendown()

brush.penup()
brush.goto(left_x_coordinate, default_price + left_y_coordinate)
brush.setheading(0)
brush.pendown()

for _ in range(y_length // 20):
    brush.forward(10)
    brush.penup()
    brush.forward(10)
    brush.pendown()

brush.setheading(0)

brush.penup()
brush.goto(left_x_coordinate, left_y_coordinate)
brush.pendown()

brush.width(3)
brush.left(60)
brush.speed(1)



brush.forward(current_price / math.cos(math.pi / 6))
brush.write(str(current_price))

brush.right(120)
brush.forward((25) / math.cos(math.pi / 6))
brush.write(str(current_price - 25))


#---------------------------#
def drawbar(step, color):
    brush.color(color)
    brush.forward(step)
    # brush.write(str(current_price))
#---------------------------#

# #---------------------------#
# if(current_price > default_price):
#     drawbar(current_price + 45, good_price_color, current_price)
# else:
#     drawbar(current_price + 45, bad_price_color, current_price)

# while True:

#     previous_price = current_price
#     current_price = random.randint(current_price - epsilon, current_price + epsilon)
#     step = abs(current_price - previous_price)

#     if previous_price > current_price and not is_up:
#         brush.right(120)
#         is_up = 1
#     elif previous_price < current_price and is_up:
#         brush.left(120)
#         is_up = 0

#     if current_price >= default_price:
#         drawbar(step, good_price_color, current_price)
#     else:
#         drawbar(step, bad_price_color, current_price)
# #---------------------------#

turtle.done()