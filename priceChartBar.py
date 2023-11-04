import turtle
import random
import math

#---Задаём общие значения---#
previous_price = 0
default_price = 300
epsilon = 20
max_value = default_price + epsilon
min_value = default_price - epsilon
current_price = random.randint(min_value, max_value)

is_up = 1

left_x_coordinate = -400
left_y_coordinate = -400

right_x_coordinate = 400
right_y_coordinate = 400

x_length = abs(left_x_coordinate) + right_x_coordinate
y_length = abs(left_y_coordinate) + right_y_coordinate

good_price_color = "green"
bad_price_color = "red"
#---------------------------#

#---Задаём настройки экрана-#
screen = turtle.Screen()
screen.setworldcoordinates(left_x_coordinate, left_y_coordinate, right_x_coordinate, right_y_coordinate)
width = x_length + 300
height = y_length - 50
screen.setup(width, height)
brush = turtle.Turtle()
#---------------------------#

#---Отрисовываем поле-------#
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
#---------------------------#

#---Отрисовка отдельной палки графика---#
def draw_stick(step, color):
    brush.color(color)
    brush.forward(step / math.cos(math.pi / 6))
#---------------------------#

#---Задаём общие характеристики для нашей кисти при отрисовке---#
brush.setheading(0)

brush.penup()
brush.goto(left_x_coordinate, left_y_coordinate)
brush.pendown()

brush.width(3)
brush.left(60)
brush.speed(1)
#---------------------------#

#---Изменение угла наклона отрисовки в зависимости от текущей стоимости---#
def check_postion():
    global is_up

    if(not is_up and previous_price < current_price):
        is_up = 1
        brush.left(120)
    elif(not is_up and previous_price >= current_price):
        is_up = 0
    elif(is_up and previous_price < current_price):
        is_up = 1
    elif(is_up and previous_price >= current_price):
        is_up = 0
        brush.right(120)
#---------------------------#

#---Отрисовка новой цены целиком---#
def draw_line():
    global previous_price
    global current_price

    if(current_price > default_price):
        if(previous_price <= default_price):
            draw_stick(default_price - previous_price, bad_price_color)
            draw_stick(current_price - default_price, good_price_color)
        else:
            draw_stick(abs(current_price - previous_price), good_price_color)
    else:
        if(previous_price > default_price):
            draw_stick(previous_price - default_price, good_price_color)
            draw_stick(default_price - current_price, bad_price_color)
        else:
            draw_stick(abs(previous_price - current_price), bad_price_color)
    # brush.write(str(current_price)) #---по желанию можно включить отрисовку значения цены на каждом шаге
    previous_price = current_price
    current_price = random.randint(previous_price - epsilon, previous_price + epsilon)
    check_postion()
#---------------------------#

while (brush.xcor() <= right_x_coordinate and current_price > 0 and current_price < 800):
    draw_line()

turtle.done()