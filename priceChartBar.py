import turtle
import random

default_price = 150
max_value = 180
min_value = 120
current_price = random.randint(min_value, max_value)
epsilon = 20
step = 15
is_up = 0

good_price_color = "green"
bad_price_color = "red"

screen = turtle.Screen()
brush = turtle.Turtle()

brush.speed(10)

brush.penup()
brush.goto(-350, -300)  # Перемещаемся в начальную точку для оси времени
brush.pendown()
brush.forward(500)  # Рисуем горизонтальную линию оси времени

# Рисуем ось стоимости
brush.penup()
brush.goto(-350, -300)  # Перемещаемся в начальную точку для оси стоимости
brush.pendown()
brush.left(90)  # Поворачиваем черепаху на 90 градусов (вертикальная линия)
brush.forward(500)  # Рисуем вертикальную линию оси стоимости

brush.penup()
brush.goto(-350,-165)
brush.right(90)
brush.pendown()

for _ in range(25):
    brush.forward(10)
    brush.penup()
    brush.forward(10)
    brush.pendown()

# Подписываем оси
brush.penup()
brush.goto(-400, 0)  # Перемещаемся для подписи оси времени
brush.write("Стоимость")

brush.goto(0, -320)  # Перемещаемся для подписи оси стоимости
brush.write("Время")


brush.goto(-350, -300)
brush.pendown()

brush.width(3)
brush.left(45)
brush.speed(1)

def drawbar(step, color, current_price):
    brush.color(color)
    brush.forward(step)
    brush.write(str(current_price))


if(current_price > default_price):
    drawbar(current_price + 40, good_price_color, current_price)
else:
    drawbar(current_price + 40, bad_price_color, current_price)

while True:

    previous_price = current_price
    current_price = random.randint(current_price - epsilon, current_price + epsilon)
    step = abs(current_price - previous_price)

    if previous_price > current_price and not is_up:
        brush.right(90)
        is_up = 1
    elif previous_price < current_price and is_up:
        brush.left(90)
        is_up = 0

    if current_price >= default_price:
        drawbar(step, good_price_color, current_price)
    else:
        drawbar(step, bad_price_color, current_price)

screen.exitonclick()