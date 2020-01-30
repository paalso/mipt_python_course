# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#id13
# Упражнение № 3: буква S

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Letter S")
    t = turtle_helper.make_turtle("red", 2)
    size = 100

    for i in range(2):
        t.forward(size)
        t.left(90)

    for i in range(3):
        t.forward(size)
        t.right(90)

    wn.mainloop()


if __name__ == '__main__':
    main()
