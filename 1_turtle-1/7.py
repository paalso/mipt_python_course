# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o7
# http://cs.mipt.ru/python/lessons/lab2.html#o7

# Упражнение № 6: спираль

import turtle
import math
import turtle_helper

def degree_to_rad(x):
    return x * math.pi / 180


def main():
    wn = turtle_helper.make_window("lightgreen", "Archimedean spiral")
    t = turtle_helper.make_turtle("red", 2)

    max_angle = 15 * 360
    step = 5
    k = 3

    for phi in range(0, max_angle, step):
        angle = degree_to_rad(phi)
        x = k * angle * math.cos(angle)
        y = k * angle * math.sin(angle)
        t.goto(x, y)

    wn.mainloop()


if __name__ == '__main__':
    main()
