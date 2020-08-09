# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o9
# Упражнение № 6: правильные многоугольники

import turtle
import turtle_helper


def draw_polygon(turtle, angles, side, start_angle):
    turtle.left(180 - start_angle)
    for i in range(angles):
        turtle.forward(side)
        turtle.left(360 / angles)

def main():
    wn = turtle_helper.make_window("lightgreen", "Spider")
    t = turtle_helper.make_turtle("red", 2)

    side = 100
    angles = 7
    start_angle = 90 - 180 / angles

    draw_polygon(t, angles, side, start_angle)



    wn.mainloop()


if __name__ == '__main__':
    main()
