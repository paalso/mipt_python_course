# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o13
# http://cs.mipt.ru/python/lessons/lab2.html#o13

# Упражнение № 11: "смайлик"

import turtle
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Smile")
    t = turtle_helper.make_turtle("black", 1, 150, 0)

    # лицо
    t.color('black', 'yellow')
    t.begin_fill()
    turtle_helper.draw_circle(t, 150, 90)
    t.end_fill()

    # глаза
    t.color('black', 'blue')
    turtle_helper.move(t, 85, 75)
    t.begin_fill()
    turtle_helper.draw_circle(t, 20, 90)
    t.end_fill()
    turtle_helper.move(t, -45, 75)
    t.begin_fill()
    turtle_helper.draw_circle(t, 20, 90)
    t.end_fill()

    # нос
    t.pensize(10)
    turtle_helper.move(t, 0, -20)
    t.color('black')
    t.forward(40)

    # рот
    turtle_helper.move(t, 80, -35)
    t.color('red')
    turtle_helper.draw_arc(t, 80, 270, 180, False)

    wn.mainloop()


if __name__ == '__main__':
    main()
