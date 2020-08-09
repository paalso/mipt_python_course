# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o10
# Упражнение № 10: "цветок"

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Flower")
    t = turtle_helper.make_turtle("red", 2)

    turtle_helper.draw_polygon(t, 10, 50, 0, counterclockwise = False)

    wn.mainloop()


if __name__ == '__main__':
    main()