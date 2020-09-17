# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o10
# http://cs.mipt.ru/python/lessons/lab2.html#o10

# Упражнение № 10: "цветок" (версия № 2)

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Flower")
    t = turtle_helper.make_turtle("red", 2)

    radius = 100

    # Используем собственную функцию draw_circle
    for angle in range(0, 360, 45):
        turtle_helper.draw_circle(t, radius, angle)

    wn.mainloop()


if __name__ == '__main__':
    main()
