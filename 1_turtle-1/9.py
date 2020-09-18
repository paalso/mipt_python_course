# http://judge.mipt.ru/mipt_cs_on_python3/labs/lab1.html#o9
# http://cs.mipt.ru/python/lessons/lab2.html#o9

# Упражнение № 6: правильные многоугольники

import turtle, math
import turtle_helper


def draw_polygon(turtle, angles, side, start_angle):
    turtle.setheading(180 - start_angle)
    for i in range(angles):
        turtle.forward(side)
        turtle.left(360 / angles)


def polygon_side_by_radius(radius, n):
    return 2 * radius * math.sin(math.pi / n)


def main():
    wn = turtle_helper.make_window("lightgreen", "Spider")
    t = turtle_helper.make_turtle("red", 2)

    x_start, y_start = 200, 0
    radius = 100
    n = 3
    side = polygon_side_by_radius(radius, 3)
    start_angle = 90 - 180 / n

    turtle_helper.move(t, x_start, y_start)
    draw_polygon(t, n, side, start_angle)

    old_radius = radius

    while n <= 10:
        n += 1
        radius = old_radius / math.cos(math.pi / n)
        dist = radius - old_radius
        turtle_helper.move(t, t.xcor() + dist, t.ycor())
        start_angle = 90 - 180 / n
        side = polygon_side_by_radius(radius, n)
        draw_polygon(t, n, side, start_angle)

        old_radius = radius

    wn.mainloop()


if __name__ == '__main__':
    main()
