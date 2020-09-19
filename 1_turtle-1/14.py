
# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o14
# http://cs.mipt.ru/python/lessons/lab2.html#o14

# Упражнение № 14: "звезды"
# Нарисуйте две звезды: одну с 5 вершинами, другую — с 11. Используйте
# функцию, рисующую звезду с n вершинами.

import turtle
import turtle_helper


def draw_star(turtle, n, k, side, start_angle):
    """
    Рисует "звезду" (звёздчатый многоугольник), где
    n - количество вершин, n >= 5
    k - порядок (количество вершин многоугольника, расположенных между двумя
    вершинами звёздного многоугольника)
    для случая gcd(n, k) == 1
    В этом и только в этом случае получается связная звезда
    Сумма углов при вершинах, которой: 180(n - 2k)
    https://habr.com/ru/post/197780/
    """
    import math
    if math.gcd(n, k) != 1:
        print("Невозможно построить связную звезду")
        return
    turtle.setheading(start_angle)
    turn_angle = 180 - (180 * (n - 2 * k)) / n
    for i in range(n):
        turtle.forward(side)
        turtle.right(turn_angle)


def main():
    wn = turtle_helper.make_window("lightgreen", "Stars")

    t = turtle_helper.make_turtle("red", 2, -250, 250)
    draw_star(t, 5, 2, 230, 18 - 90)

    turtle_helper.move(t, 120, -120)
    t.color("blue")

    draw_star(t, 11, 4, 230, 0)

    wn.mainloop()


if __name__ == '__main__':
    main()
