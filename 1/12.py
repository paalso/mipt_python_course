# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o12
# Упражнение № 11: "пружина"

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Flower")
    t = turtle_helper.make_turtle("red", 2, -350, 0)


    for i in range(4):
        turtle_helper.draw_arc(t, 80, 90, 180, False)
        turtle_helper.draw_arc(t, 15, 270, 180, False)

    turtle_helper.draw_arc(t, 80, 90, 180, False)

    wn.mainloop()


if __name__ == '__main__':
    main()
