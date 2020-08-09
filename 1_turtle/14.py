# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o14
# Упражнение № 11: "звезды"

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", Stars")
    t = turtle_helper.make_turtle("black", 2, -250, 100)

    t.right(72)
    for i in range(5):
        t.forward(250)
        t.right(180 - 36)

    turtle_helper.move(t, 250, 100)
    t.right(72)

    wn.mainloop()


if __name__ == '__main__':
    main()
