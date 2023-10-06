import turtle
import time

screen = turtle.Screen()
width=1280
height=720
screen.setup(width, height)

current_angle = 0

gun = turtle.Turtle()
gun_position_x = -560
gun_position_y = - 280

gun.speed(0)
gun.shape("square")
gun.shapesize(2,5)
gun.penup()
gun.goto(gun_position_x, gun_position_y)


bullet = turtle.Turtle()
bullet_position_x = gun_position_x
bullet_position_y = gun_position_y
current_buller_time = 0

bullet.penup()
bullet.speed(0)
bullet.shape("circle")
bullet.goto(bullet_position_x, bullet_position_y)

def angle_up():
    global current_angle

    if current_angle >= 90:
        current_angle = 90
    else:
        current_angle += 10

    gun.setheading(current_angle)

def angle_down():
    global current_angle

    if current_angle <= 0:
        current_angle = 0
    else:
        current_angle -= 10

    gun.setheading(current_angle)

def fire_bullet():
    global bullet_position_x
    global current_buller_time

    while bullet_position_x != width/2:
        bullet_position_x += 10
        bullet.goto(bullet_position_x, bullet_position_y)

        current_buller_time += 0.01
        time.sleep(current_buller_time)  # Подождите некоторое время
        screen.update()

screen.onkey(angle_up, "w")
screen.onkey(angle_down, "s")
screen.onkey(fire_bullet, "q")
screen.listen()

turtle.done()