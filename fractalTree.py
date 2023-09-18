import turtle

def draw_tree(branch_length, t):
    if branch_length > 5:
        # Рисуем основную ветку
        t.forward(branch_length)

        # Поворачиваемся вправо
        t.right(20)

        # Рисуем правую подветку рекурсивно
        draw_tree(branch_length - 15, t)

        # Поворачиваемся влево (в исходное положение)
        t.left(40)

        # Рисуем левую подветку рекурсивно
        draw_tree(branch_length - 15, t)

        # Возвращаемся в исходное положение
        t.right(20)

        # Перемещаемся обратно к начальной точке
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    
    t = turtle.Turtle()
    t.speed(0)  # Максимальная скорость рисования
    
    # Поднимаем перо и перемещаемся в начальную позицию
    t.penup()
    t.goto(0, -200)
    t.pendown()

    # Устанавливаем угол обзора
    t.setheading(90)

    # Устанавливаем глубину рекурсии и длину начальной ветки
    depth = 3
    initial_branch_length = 100

    draw_tree(initial_branch_length, t)

    screen.exitonclick()

if __name__ == "__main__":
    main()
