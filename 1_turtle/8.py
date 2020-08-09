# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o8
# Упражнение № 6: квадратная спираль

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Quadratic spiral")
    t = turtle_helper.make_turtle("red", 2)

    segment = 10
    step = 5

    for i in range(60):
        t.forward(segment)
        t.left(90)
        segment += step

    wn.mainloop()


if __name__ == '__main__':
    main()
