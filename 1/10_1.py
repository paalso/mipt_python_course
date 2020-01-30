# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o10
# Упражнение № 10: "цветок" (версия № 1)

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Flower")
    t = turtle_helper.make_turtle("red", 2)

# Используем стандартный метод circle
    side = 100
    t.circle(100)
    t.circle(-100)
    t.left(90)
    t.circle(100)
    t.circle(-100)
    t.left(45)
    t.circle(100)
    t.circle(-100)
    t.right(90)
    t.circle(100)
    t.circle(-100)

    wn.mainloop()


if __name__ == '__main__':
    main()
