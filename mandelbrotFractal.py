import turtle
import math

#---Настройки окна----------------#
screen = turtle.Screen()
width = 400
height = 400
screen.setup(width, height)
screen.bgcolor("white")
#---------------------------------#

brush = turtle.Turtle()
brush.speed(0)
turtle.tracer(10000, None)

P = 200                     #размер [2*P +1 x 2*P + 1]
scale = P / 2               #коэффициент масштабирования
number_of_iteration = 200   #количество итераций
color_coefficient = 0.003921568627451
x_shift = 0
y_shift = 0

def draw_fractal(P, scale, number_of_iteration):
    brush.reset()

    for y in range(-P - y_shift, P - y_shift):
        for x in range(-P - x_shift, P - x_shift):
            a = x / scale
            b = y / scale
            c = complex(a, b)
            z = complex(0)
            i = 0

            #---проверка на нужное число--------#
            for i in range(number_of_iteration):
                z = z**2 + c

                if abs(z) > 2:
                    break
            #-----------------------------------#
            if i == number_of_iteration - 1:
                draw_dot(x,y,0,0,0)

#---Функция отрисовки каждой точки------------#
def draw_dot(x,y,r,g,b):
    brush.penup()
    brush.goto(x + x_shift, y + y_shift)
    brush.pendown()
    brush.color(r,g,b)
    brush.dot(2)
#---------------------------------------------#

#---Увеличение/Уменьшение картинки------------#
def scale_up():
    global scale
    scale = scale * 1.2
    draw_fractal(P, scale, number_of_iteration)

def scale_down():
    global scale
    scale = scale / 1.2
    draw_fractal(P, scale, number_of_iteration)
#---------------------------------------------#

#---Сдвиг Влево/Вправо/Вверх/Вниз-------------#
def shift_left():
    global x_shift
    x_shift = x_shift - 50
    draw_fractal(P, scale, number_of_iteration)

def shift_right():
    global x_shift
    x_shift = x_shift + 50
    draw_fractal(P, scale, number_of_iteration)

def shift_up():
    global y_shift
    y_shift = y_shift + 50
    draw_fractal(P, scale, number_of_iteration)

def shift_down():
    global y_shift
    y_shift = y_shift - 50
    draw_fractal(P, scale, number_of_iteration)
#---------------------------------------------#

draw_fractal(P, scale, number_of_iteration)

screen.listen()
screen.onkey(scale_up, "=")
screen.onkey(scale_down, "-")
screen.onkey(shift_left, "Left")
screen.onkey(shift_right, "Right")
screen.onkey(shift_up, "Up")
screen.onkey(shift_down, "Down")

turtle.done()
