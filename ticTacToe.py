import turtle
import time as t

#------------------------------------------#
screen = turtle.Screen()
width = 700
height = 700
screen.setup(width, height)
brush = turtle.Turtle()
brush.speed(0)
#------------------------------------------#

#---Объявление массива 3х3, объявление цифровых значений х и о---#
n = 3
tic_tac_toe_field = [[0] * n for _ in range(n)]
x_value = 1
o_value = 2
is_match = False
is_cell_empty = True
#------------------------------------------#

#------------------------------------------#
current_x_cell = 0
current_y_cell = 1
is_clicked = False
is_x_first = False

border_width = width * 0.8
border_height = height * 0.8

top_border = border_height / 2
bottom_border = - border_height / 2

left_border = - border_width / 2
right_border = border_width / 2

first_row_border = border_height / 6
second_row_border = - border_height / 6

first_column_border = -border_width / 6
second_column_border = border_width / 6

first_column_figure_coordinate = - border_width / 3
second_column_figure_coordinate = 0
third_column_figure_coordinate = border_width / 3

first_row_figure_coordinate = border_height / 4
second_row_figure_coordinate = - border_height / 12
third_row_figure_coordinate = - 5 * border_height / 12

circle_radius = border_height / 12
cross_length = border_height / 5
#------------------------------------------#

#------------------------------------------#
def draw_line (width, height, length):
    brush.penup()
    brush.goto(width, height)
    brush.pendown()
    brush.forward(length)

brush.left(90)
draw_line(first_column_border, bottom_border, border_height)
draw_line(second_column_border, bottom_border, border_height)
brush.right(90)
draw_line(left_border, first_row_border, border_width)
draw_line(left_border, second_row_border, border_width)
#------------------------------------------#

#------------------------------------------#
first_turn = screen.textinput("Кто первый ходит?", "Введите X или O")

if first_turn == 'X':
    is_x_first = True
elif first_turn == 'O':
    is_x_first = False
#------------------------------------------#    

#---Обработка клика, определение координат и занесение в массив значения элемента---#
def on_click(x, y):
    global is_x_first
    global tic_tac_toe_field
    global current_x_cell
    global current_y_cell
    global is_clicked
    global is_cell_empty

    is_cell_empty = True
    is_clicked = True

    if x > first_column_border:
        if x > second_column_border:
            x = 2
            current_x_cell = third_column_figure_coordinate
        else:
            x = 1
            current_x_cell = second_column_figure_coordinate
    else:
        x = 0
        current_x_cell = first_column_figure_coordinate
    
    if y < first_row_border:
        if y < second_row_border:
            y = 2
            current_y_cell = third_row_figure_coordinate
        else:
            y = 1
            current_y_cell = second_row_figure_coordinate
    else:
        y = 0
        current_y_cell = first_row_figure_coordinate

    if tic_tac_toe_field[y][x] == 0:
        if is_x_first:
            tic_tac_toe_field[y][x] = x_value
        else:
            tic_tac_toe_field[y][x] = o_value
    else:
        print("Эта ячейка уже занята!")
        is_cell_empty = False
#------------------------------------------#

#---Проверка на выигрыш--------------------#
def detect_match(tic_tac_toe_field, value):
    global is_match

    #---проверка на выигрыш по рядам---#
    for i in range(0, 3):
        is_match = True
        for j in range(0, 3):
            if tic_tac_toe_field[i][j] != value:
                is_match = False
                print(i, j)
        
        if is_match:
            break
    
    #---проверка на выигрыш по столбцам---#
    if(not is_match):
        for j in range(0,3):
            is_match = True
            for i in range(0,3):
                if tic_tac_toe_field[i][j] != value:
                    is_match = False
            
            if is_match:
                break

    #---проверка на выигрыш по диагонали---#
    if(not is_match):
        is_match = True
        for i in range(0,3):
            if tic_tac_toe_field[i][i] != value:
                is_match = False

    #---проверка на выигрыш по обратной диагонали---#
    if(not is_match):
        is_match = True
        if tic_tac_toe_field[0][2] != value:
            is_match = False
        if tic_tac_toe_field[1][1] != value:
            is_match = False
        if tic_tac_toe_field[2][0] != value:
            is_match = False   

    print(is_match)
    #---проверка, есть ли в массиве нули (если нет, то это либо кто-то выиграл, либо ничья)---#
    is_full = True
    for i in range(0,3):
        for j in range(0,3):
            if tic_tac_toe_field[i][j] == 0:
                is_full = False

    if is_match and not is_full:
        print("Игра окончена\nПобедили: ", end='')
        
        if value == x_value:
            print("крестики!")
        else:
            print("нолики!")

    elif not is_match and is_full:
        print("Игра окончена!\nНичья!")
        is_match = True

    elif is_match and is_full:
        print("Игра окончена\nПобедили: ", end='')
        
        if value == x_value:
            print("крестики!")
        else:
            print("нолики!")

    else:
        print("Пока никто не выиграл!")
        print("Текущее положение:")
        for i in range(0,3):
            for j in range(0,3):
                print(tic_tac_toe_field[i][j], end='')
            print()
#------------------------------------------#

#------------------------------------------#
def draw_x (x_position_x, x_position_y):
    brush.color("red")
    brush.penup()
    brush.width(3)
    brush.goto(x_position_x - 43, x_position_y)
    brush.pendown()
    brush.setheading(45)
    brush.forward(cross_length)
    brush.penup()
    brush.goto(x_position_x + 43, x_position_y)
    brush.pendown()
    brush.left(90)
    brush.forward(cross_length)
#------------------------------------------#

#------------------------------------------#
def draw_o (o_position_x, o_position_y):
    brush.setheading(0)
    brush.color("blue")
    brush.penup()
    brush.goto(o_position_x, o_position_y)
    brush.width(3)
    brush.pendown()
    brush.circle(circle_radius)
#------------------------------------------#

#------------------------------------------#
screen.onscreenclick(on_click)

def wait_for_click():
    global is_clicked

    screen.update()
    is_clicked = False

    while not is_clicked:
        screen.update()
        t.sleep(.1)

    is_clicked = False

screen.update()
#------------------------------------------#

#------------------------------------------#
while(not is_match):

    if(is_x_first):
        print("Сейчас ходят Крестики!")
    else:
        print("Сейчас ходят Нолики!")

    wait_for_click()

    if is_cell_empty:
        if is_x_first:
            draw_x(current_x_cell, current_y_cell)
            detect_match(tic_tac_toe_field, x_value)
        else:
            draw_o(current_x_cell, current_y_cell)
            detect_match(tic_tac_toe_field, o_value)

        is_x_first = not is_x_first
#------------------------------------------#

screen.onscreenclick(None)
turtle.done()