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

empty_tile_sign = 0
filled_tile_sign = 1

is_over = False
#------------------------------------------------#

#---Создание поля и фигур------------------------#
black = (0,0,0)

grid = [pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size) for x in range(tiles_x) for y in range(tiles_y)]

figures_position = [[(-2,0), (-1,0), (0,0), (1,0)],    # @@@@
                
                    [(-1,-1), (0,-1), (-1,0), (0,0)],  # @@
                                                       # @@
                
                    [(-1,1), (-1,0), (0,0), (0,-1)],   #  @
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

                    [(-1,0), (0,0), (0,-1), (0,1)]]    #  @
                                                       # @@
                                                       #  @

figures = [[pygame.Rect(x + tiles_x // 2, y + 1, 1, 1) for x,y in figure_position] for figure_position in figures_position]

figure_rect = pygame.Rect(0,0, tile_size - 2, tile_size - 2)


random_index = random.randint(0,6)
current_figure = [pygame.Rect(rect.x, rect.y, rect.width, rect.height) for rect in figures[random_index]]


current_field = [[0] * tiles_x for _ in range(tiles_y)]
#------------------------------------------------#

def checking_rows():
    for y in range(tiles_y - 1, -1, -1):
        is_row_full = True

        for x in range(tiles_x):
            if not current_field[y][x]:
                is_row_full = False
                break

        if is_row_full:
            for i in range(y, 0, -1):
                for j in range(tiles_x):
                    current_field[i][j] = current_field[i - 1][j]

            for j in range(tiles_x):
                current_field[0][j] = 0

#---Отрисовка фигуры с учётом изменений---#
def draw_current_figure():
    for i in range(4):
        figure_rect.x = current_figure[i].x * tile_size
        figure_rect.y = current_figure[i].y * tile_size
        pygame.draw.rect(screen, pygame.Color('white'), figure_rect)

#---Отрисовка текущего поля---#
def draw_current_field():
    for y in range(tiles_y):
        for x in range(tiles_x):
            if current_field[y][x] != 0:
                pygame.draw.rect(screen, pygame.Color('white'), (x * tile_size, y * tile_size, tile_size, tile_size))

def rotate_figure(clockwise):
    center_x = current_figure[1].x
    center_y = current_figure[1].y

    for i in range(4):
        relative_x = current_figure[i].x - center_x
        relative_y = current_figure[i].y - center_y

        if clockwise:
            new_x = center_x - relative_y
            new_y = center_y + relative_x
        else:
            new_x = center_x + relative_y
            new_y = center_y - relative_x

        if not (0 <= new_x < tiles_x and 0 <= new_y < tiles_y):
            break
    else:
        for i in range(4):
            relative_x = current_figure[i].x - center_x
            relative_y = current_figure[i].y - center_y

            if clockwise:
                current_figure[i].x = center_x - relative_y
                current_figure[i].y = center_y + relative_x
            else:
                current_figure[i].x = center_x + relative_y
                current_figure[i].y = center_y - relative_x

#---Цикл игры-----------------------------------#
while not is_over:
    
    dx = 0
    is_rotate = False
    is_bottom = False

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
            elif event.key == pygame.K_q:
                is_rotate = True
                rotate_figure(clockwise=False)
            elif event.key == pygame.K_e:
                rotate_figure(clockwise=True)

    #----------------------#

    #---Обработка смещения по x---#
    for rect in current_figure:
        if not ((0 <= rect.x + dx < tiles_x) and current_field[rect.y][rect.x + dx] != filled_tile_sign):
            break
    else:
        for rect in current_figure:
            rect.x += dx
    #-----------------------------#

    #---Обработка смещения по y---#
    current_time = pygame.time.get_ticks()

    for i in range(4):
        if current_figure[i].y + 1 >= tiles_y or current_field[current_figure[i].y + 1][current_figure[i].x] == filled_tile_sign:
            is_bottom = True
            break
    
    if is_bottom or (current_time - fall_time > fall_delay):
        fall_time = current_time
        if not is_bottom:
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

    for i in range(4):
        if current_figure[i].y == 0 and current_field[current_figure[i].y + 1][current_figure[i].x] == filled_tile_sign:
            is_over = True
            print("Игра окончена!")
            break


    #Отрисовка карты
    [pygame.draw.rect(screen, (40,40,40), i_rect, 1) for i_rect in grid]

    checking_rows()

    draw_current_field()

    draw_current_figure()

    pygame.display.flip()
    clock.tick(FPS)
#-----------------------------------------------#