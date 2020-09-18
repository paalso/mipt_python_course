# http://cs.mipt.ru/python/lessons/lab3.html#id4

# Упражнение № 1

import turtle, random
import turtle_helper


def main():
    wn = turtle_helper.make_window("lightgreen", "Letter S")
    t = turtle_helper.make_turtle("red", 2)

    max_step_len = 25
    steps_qty = 100

    for i in range(steps_qty):
        t.forward(int(max_step_len * random.random()))
        to_left = 1 if random.random() < 0.5 else -1
        t.left(to_left * int(180 * random.random()))


    wn.mainloop()


if __name__ == '__main__':
    main()
