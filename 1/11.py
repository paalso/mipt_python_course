# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o11
# Упражнение № 11: "бабочка"

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Flower")
    t = turtle_helper.make_turtle("red", 2)

    radius = 60
    step = 10

    # Используем собственную функцию draw_circle
    for i in range(10):
        radius += step
        turtle_helper.draw_circle(t, radius, 90)
        turtle_helper.draw_circle(t, radius, 90, counterclockwise = False)

    wn.mainloop()


if __name__ == '__main__':
    main()
