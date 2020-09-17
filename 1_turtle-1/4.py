# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o4
# http://cs.mipt.ru/python/lessons/lab2.html#o4

# Упражнение № 4: окружность

import turtle
import math
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Circle")
    t = turtle_helper.make_turtle("red", 2, -70, -130)

    SIDES_QTY = 35
    DIAM = 300

    side = round(math.pi * DIAM / SIDES_QTY)
    angle = 360 / SIDES_QTY

    for i in range(SIDES_QTY):
        t.forward(side)
        t.left(angle)

    wn.mainloop()


if __name__ == '__main__':
    main()