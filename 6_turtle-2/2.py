# http://cs.mipt.ru/python/lessons/lab3.html#id9

# Упражнение № 2

import turtle, random
import turtle_helper


def print_digit(t, d, step):

    gap = int(0.4 * step)
    sqrt2 = 2 ** 0.5
    font = {
        "0" : [(1, 0, 1), (1, -90, 2), (1, 180, 1), (1, 90, 2), (0, 0, 1)],
        "1" : [(0, -90, 1), (1, 45, sqrt2), (0, -90, 2), (1, 90, 2)],
        "2" : [(1, 0, 1), (1, -90, 1), (1, -135, sqrt2), (1, 0, 1), (0, 90, 2)],
        "3" : [(1, 0, 1), (1, -135, sqrt2), (1, 0, 1), (1, -135, sqrt2),
                (0, 0, 1), (0, 90, 2)],
        "4" : [(1, -90, 1), (1, 0, 1), (0, -90, 1), (1, 90, 2)],
        "5" : [(0, 0, 1), (1, 180, 1), (1, -90, 1), (1, 0, 1), (1, -90, 1),
                (1, 180, 1), (0, 0, 1), (0, 90, 2)],
        "6" : [(0, -90, 1), (1, 0, 1), (1, -90, 1), (1, 180, 1), (1, 90, 1),
                (1, 45, sqrt2)],
        "7" : [(1, 0, 1), (1, -135, sqrt2), (1, -90, 1), (0, 0, 1), (0, 90, 2)],
        "0" : [(1, 0, 1), (1, -90, 2), (1, 180, 1), (1, 90, 2), (0, 0, 1)],
        "8" : [(1, 0, 1), (1, -90, 2), (1, 180, 1), (1, 90, 2), (0, -90, 1),
                (1, 0, 1), (0, 90, 1)],
        "9" : [(0, -90, 2), (1, 45, sqrt2), (1, 180, 1), (1, 90, 1), (1, 0, 1),
                (1, -90, 1), (1, 90, 1)]
    }

    def move_gap():
        t.penup(); t.setheading(0); t.fd(gap); t.pendown()

    for pen_down, angle, step_quot in font[d]:
        if not pen_down: t.penup()
        t.setheading(angle)
        t.fd(step_quot * step)
        t.pendown()
    move_gap()


def print_index_style(t, digits_str, step):
    digits_str = str(digits_str)     # if type(digits_str) == int
    t.speed(8)
    for d in digits_str:
        print_digit(t, d, step)


def main():
    wn = turtle_helper.make_window("lightgreen", "Letter S")
    t = turtle_helper.make_turtle("red", 2, shape="classic")
    turtle_helper.move(t, -350, 0)
    print_index_style(t, "02123475297516589", 30)

    wn.mainloop()


if __name__ == '__main__':
    main()
