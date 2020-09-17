# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o6
# http://cs.mipt.ru/python/lessons/lab2.html#o6

# Упражнение № 6: паук

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Spider")
    t = turtle_helper.make_turtle("red", 2)

    ARMS_QTY = 13

    length = 200
    angle = 360 / ARMS_QTY

    x, y = -100, -50
    for i in range(ARMS_QTY):
        t.forward(length)
        t.stamp()
        t.left(180)
        t.forward(length)
        t.left(180)
        t.left(angle)

    wn.mainloop()


if __name__ == '__main__':
    main()
