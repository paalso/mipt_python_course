# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o3
# http://cs.mipt.ru/python/lessons/lab2.html#o3

# Упражнение № 3: квадрат

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Square")
    t = turtle_helper.make_turtle("red", 2)
    size = 100

    for i in range(4):
        t.forward(size)
        t.left(90)


    wn.mainloop()


if __name__ == '__main__':
    main()
