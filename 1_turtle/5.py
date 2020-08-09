# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o5
# Упражнение №5: больше квадратов

import turtle
import turtle_helper

def paint_square(turtle, side, x = 0, y = 0, angle = 0):
    turtle_helper.move(turtle, x, y)
    turtle.left(angle)
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)


def main():
    wn = turtle_helper.make_window("lightgreen", "More squares")
    t = turtle_helper.make_turtle("red", 2, -50, -100)

    SQUARES_QTY = 10

    side = 40
    side_shift = 15

    x, y = -100, -50
    for i in range(SQUARES_QTY):
        paint_square(t, side, x, y)
        side += 2 * side_shift
        x -= side_shift
        y -= side_shift

    wn.mainloop()


if __name__ == '__main__':
    main()
