import turtle
import time
import math

#---Создаем экран-------------#
screen = turtle.Screen()
screen.title("Аналоговые часы")
#-----------------------------#

#---Создаем часовую стрелку---#
hour_hand = turtle.Turtle()
hour_hand.shape("square")
hour_hand.shapesize(0.3, 4)
hour_hand.color("blue")
#-----------------------------#

#---Создаем минутную стрелку--#
minute_hand = turtle.Turtle()
minute_hand.shape("square")
minute_hand.shapesize(0.3, 5)
minute_hand.color("green")
#-----------------------------#

#---Создаем секундную стрелку-#
second_hand = turtle.Turtle()
second_hand.shape("square")
second_hand.shapesize(0.2, 6)
second_hand.color("red")
#-----------------------------#

#---Рисуем циферблат----------#
def draw_clock_face():
    clock_face = turtle.Turtle()
    clock_face.penup()
    clock_face.speed(0)
    clock_face.color("black")

    for hour in range(1, 13):
        angle = 95.8 + math.radians(360 / 12 * (12 - hour))
        x = 150 * math.cos(angle)
        y = 150 * math.sin(angle)
        clock_face.goto(x, y - 10)
        clock_face.write(str(hour), align="center", font=("Arial", 12, "normal"))

    clock_face.hideturtle()
#-----------------------------#

#---Функция для обновления времени и анимации стрелок---#
def update_clock():
    while True:
        current_time = time.localtime()
        seconds = current_time.tm_sec
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min

        #---Устанавливаем часовую стрелку---#
        hour_hand.hideturtle()
        hour_hand.penup()
        hour_hand.goto(0,0)
        hour_angle = 90 - (360 / 12) * hours - (360 / 12) * (minutes / 60)
        hour_hand.setheading(hour_angle)
        hour_hand.forward(40)
        hour_hand.showturtle()   

        #---Устанавливаем минутную стрелку---#
        minute_hand.hideturtle()
        minute_hand.penup()
        minute_hand.goto(0,0)
        minute_angle = 90 - (360 / 60) * minutes
        minute_hand.setheading(minute_angle)
        minute_hand.forward(50)
        minute_hand.showturtle()   

        #---Устанавливаем секундную стрелку---#
        second_hand.hideturtle()
        second_hand.penup()
        second_hand.goto(0,0)
        second_angle = 90 - (360 / 60) * seconds
        second_hand.setheading(second_angle)
        second_hand.forward(60)
        second_hand.showturtle()   

        time.sleep(0.5)
#-----------------------------#

draw_clock_face()
update_clock()
turtle.mainloop()