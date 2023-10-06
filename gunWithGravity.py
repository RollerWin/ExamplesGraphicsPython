import turtle
import math

#---Настройки окна----------------#
screen = turtle.Screen()
width=1280
height=720
screen.setup(width, height)
#---------------------------------#

#---Создаём пушку-----------------#
gun = turtle.Turtle()

gun_position_x = -560
gun_position_y = - 280
current_angle = 0
rotation_speed = 5

gun.speed(0)
gun.shape("square")
gun.shapesize(2,5)
gun.penup()
gun.goto(gun_position_x, gun_position_y)
gun.setheading(current_angle)
#---------------------------------#

#---Создаём класс пули и список пуль---#
bullets = []

class Bullet(turtle.Turtle):
    def __init__(self, x, y, angle):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.shape("circle")
        self.speed(0)
        self.showturtle()
        self.angle = angle
        self.velocity = 40
        self.time_interval = 0.1
        self.g = 50  # Ускорение свободного падения (м/с^2)

    # Метод для движения снаряда
    def move(self):
        # Рассчитываем новые координаты снаряда
        x = self.xcor() + self.velocity * self.time_interval * math.cos(math.radians(self.angle))
        y = self.ycor() + self.velocity * self.time_interval * math.sin(math.radians(self.angle)) - 0.5 * self.g * (self.time_interval ** 2)

        self.goto(x, y)
#---------------------------------#

#---Методы для поворота пушки-----#
def gun_up():
    if gun.heading() < 90:
        gun.setheading(gun.heading() + rotation_speed)

def gun_down():
    if gun.heading() > 0:
        gun.setheading(gun.heading() - rotation_speed)
#---------------------------------#

#---------------------------------#
def fire_bullet(x, y):
    if -300 < y < -260 and -600 < x < 520:
        angle = gun.heading()
        x = gun.xcor()
        y = gun.ycor()
        bullet = Bullet(x, y, angle)
        bullets.append(bullet)  # Добавляем снаряд в список активных снарядов

#---------------------------------#

screen.listen()
screen.onkey(gun_up, "Up")
screen.onkey(gun_down, "Down")
# screen.onkey(fire_bullet, "space")
screen.onclick(fire_bullet)

# Запуск главного цикла программы
while True:
    # Двигаем все активные снаряды
    for bullet in bullets:
        bullet.move()
        
        # Проверяем, вышел ли снаряд за пределы экрана
        if bullet.ycor() > height / 2 or bullet.xcor() > width / 2 or bullet.ycor() < - height / 2:
            bullet.hideturtle()
            bullets.remove(bullet)

    screen.update()