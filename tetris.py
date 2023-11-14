import pygame
import random

#---Задание параметров экрана-------------------#
pygame.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Тетрис")

tiles_x = 10
tiles_y = 20
tile_size = 40

width = tiles_x * tile_size
height = tiles_y * tile_size
screen = pygame.display.set_mode((width, height))

FPS = 60

fall_time = 0
default_fall_delay = 1000
fall_delay = default_fall_delay
#------------------------------------------------#

#---Создание поля и фигур------------------------#
black = (0,0,0)

grid = [pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size) for x in range(tiles_x) for y in range(tiles_y)]

figures_position = [[(-2,0), (-1,0), (0,0), (1,0)],    # @@@@
                
                    [(-1,-1), (0,-1), (-1,0), (0,0)],  # @@
                                                       # @@
                
                    [(-1,0), (-1,1), (0,0), (0,-1)],   #  @
                                                       # @@
                                                       # @

                    [(-1,-1), (-1,0), (0,1), (0,0)],   # @
                                                       # @@
                                                       #  @

                    [(-1,-1), (0,-1), (0,1), (0,0)],   # @@
                                                       #  @
                                                       #  @

                    [(-1,0), (-1,-1), (-1,1), (0,-1)], # @@
                                                       # @
                                                       # @

                    [(-1,0), (0,-1), (0,1), (0,0)]]    #  @
                                                       # @@
                                                       #  @

figures = [[pygame.Rect(x + tiles_x // 2, y + 1, 1, 1) for x,y in figure_position] for figure_position in figures_position]

figure_rect = pygame.Rect(0,0, tile_size - 2, tile_size - 2)


random_index = random.randint(0,6)
current_figure = [pygame.Rect(rect.x, rect.y, rect.width, rect.height) for rect in figures[random_index]]


current_field = [[0] * tiles_x for _ in range(tiles_y)]
#------------------------------------------------#

def draw_current_figure():
    #---Отрисовка фигуры с учётом изменений---#
    for i in range(4):
        figure_rect.x = current_figure[i].x * tile_size
        figure_rect.y = current_figure[i].y * tile_size
        pygame.draw.rect(screen, pygame.Color('white'), figure_rect)

def draw_current_field():
    #---Отрисовка текущего поля---#
    for y in range(tiles_y):
        for x in range(tiles_x):
            if current_field[y][x] != 0:
                pygame.draw.rect(screen, pygame.Color('white'), (x * tile_size, y * tile_size, tile_size, tile_size))
    #-----------------------------#


#---Цикл игры-----------------------------------#
while True:
    
    dx = 0
    is_rotate = False

    screen.fill(black)

    #---Обработка клавиш---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_DOWN:
                fall_delay /= 5
            elif event.key == pygame.K_UP:
                is_rotate = True

    #----------------------#

    #---Обработка смещения по x---#
    if(not(current_figure[0].x + dx < 0 or current_figure[3].x + dx > tiles_x - 1)):
        for i in range(4):
            current_figure[i].x += dx
    #-----------------------------#

    #---Обработка смещения по y---#
    current_time = pygame.time.get_ticks()

    at_bottom = False
    for i in range(4):
        if current_figure[i].y + 1 >= tiles_y or current_field[current_figure[i].y + 1][current_figure[i].x] != 0:
            at_bottom = True
            break
    
    if at_bottom or (current_time - fall_time > fall_delay):
        fall_time = current_time
        if not at_bottom:
            for i in range(4):
                current_figure[i].y += 1
        else:
            for i in range(4):
                current_field[current_figure[i].y][current_figure[i].x] = 1

            for i in range(tiles_y):
                for j in range(tiles_x):
                    print(current_field[i][j], end='')
                print()

            print()

            random_index = random.randint(0,6)
            current_figure = [pygame.Rect(rect.x, rect.y, rect.width, rect.height) for rect in figures[random_index]]
            fall_delay = default_fall_delay
    #-----------------------------#

    for y in range(tiles_y - 1, -1, -1):
        is_row_full = True

        for x in range(tiles_x):
            if not current_field[y][x]:
                is_row_full = False
                break

        if is_row_full:
            # Сдвигаем все строки выше текущей вниз
            for i in range(y, 0, -1):
                for j in range(tiles_x):
                    current_field[i][j] = current_field[i - 1][j]

            # Заполняем верхнюю строку нулями
            for j in range(tiles_x):
                current_field[0][j] = 0

    #Отрисовка карты
    [pygame.draw.rect(screen, (40,40,40), i_rect, 1) for i_rect in grid]
    
    draw_current_field()

    draw_current_figure()

    pygame.display.flip()
    clock.tick(FPS)
#-----------------------------------------------#