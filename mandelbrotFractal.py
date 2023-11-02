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
turtle.tracer(100000, None)

P = 200                     #размер [2*P +1 x 2*P + 1]
scale = P / 2               #коэффициент масштабирования
number_of_iteration = 100   #количество итераций
color_coefficient = 0.003921568627451

def draw_fractal(P, scale, number_of_iteration):
    for y in range(-P, P):
        for x in range(-P, P):
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
                brush.penup()
                brush.goto(x, y)
                brush.pendown()
                brush.color("black")
                brush.dot()
            # else:
            #     r = color_coefficient * ((i%2) * 32 + 128)
            #     g = color_coefficient * ((i%4) * 64)
            #     b = color_coefficient * ((i%2) * 16 + 128)
                    
            #     brush.penup()
            #     brush.goto(x, y)
            #     brush.pendown()
            #     brush.color(r,g,b)
            #     brush.dot()

def scale_up():
    global scale

    screen.clear()
    
    scale /= 2
    draw_fractal(P, scale, number_of_iteration)

def scale_down():
    global scale

    screen.clear()
    
    scale *= 2
    draw_fractal(P, scale, number_of_iteration)

draw_fractal(P, scale, number_of_iteration)

screen.listen()
screen.onkey(scale_up, "Up")
screen.onkey(scale_down, "Down")

turtle.done()
