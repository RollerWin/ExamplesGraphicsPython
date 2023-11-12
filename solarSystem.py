import pygame
import sys
import math

#---Задание параметров экрана-------------------#
pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
FPS = 60
pygame.display.set_caption("Солнечная система")
#-----------------------------------------------#

#---Цвета для планет----------------------------#
black = (0, 0, 0)
yellow = (255, 255, 0)
mercury_color = (169, 169, 169)
venus_color = (255, 165, 0)
earth_color = (0, 200, 255)
mars_color = (255, 0, 0)
jupiter_color = (221,180,126)
saturn_color = (195,146,79)
uranus_color = 	(147,205,241)
neptune_color = (61,94,249)
#-----------------------------------------------#

#---Класс планеты и функция её отрисовки и движения---#
class Planet:
    def __init__(self, color, radius, distance, speed):
        self.color = color
        self.radius = radius
        self.distance = distance
        self.angle = 0
        self.speed = speed

    def draw(self):
        x = width // 2 + int(self.distance * math.cos(math.radians(self.angle)))
        y = height // 2 + int(self.distance * math.sin(math.radians(self.angle)))
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

    def update(self):
        self.angle += self.speed
#-----------------------------------------------#

#---Класс солнца и функция её отрисовки---------#
class Sun:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, self.color, (width // 2, height // 2), self.radius)
#-----------------------------------------------#

#---Инициализация планет------------------------#
sun = Sun(yellow, 40)
mercury = Planet(mercury_color, 5, 50, 2)
venus = Planet(venus_color, 8, 80, 1.5)
earth = Planet(earth_color, 10, 110, 1)
mars = Planet(mars_color, 6, 150, 0.8)
jupiter = Planet(jupiter_color, 25, 200, 0.4)
saturn = Planet(saturn_color, 20, 280, 0.3)
uranus = Planet(uranus_color, 15, 360, 0.2)
neptune = Planet(neptune_color, 12, 400, 0.1)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
#-----------------------------------------------#

#---Цикл игры-----------------------------------#
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    sun.draw()

    for planet in planets:
        planet.update()
        planet.draw()

    pygame.display.flip()
    clock.tick(FPS)
#-----------------------------------------------#