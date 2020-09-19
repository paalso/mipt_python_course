import turtle
import math
import turtle_helper
import particle


def check_near_borders(window, turtle):
    x_min, x_max = - wn.window_width() // 2, wn.window_width() // 2
    y_min, y_max = - wn.window_height() // 2, wn.window_height() // 2
    x, y = turtle.xcor(), turtle.ycor()


def max_flight_range(v0, alpha, a):
    return v0 * v0 / a * math.sin(2 * math.radians(alpha))


def main():
    v0, alpha = 90, 45
##    print(max_flight_range(v0, alpha, 10))

    p = particle.Vector(0, 0)
    v = particle.Vector( v0 * math.cos(math.radians(alpha)),
                v0 * math.sin(math.radians(alpha)))
    a = particle.Vector(0, -10)
    ball = particle.Particle(p, v, a)

    wn = turtle_helper.make_window("lightgreen", "Cannon shooting")
    wn.setworldcoordinates(0, 0, 1000, 850)
    turtle = turtle_helper.make_turtle("blue", 0, 0, shape="circle")
    turtle.speed(3)


    # Исходные данные
    x_min, x_max = - wn.window_width() // 2, wn.window_width() // 2
    y_min, y_max = - wn.window_height() // 2, wn.window_height() // 2

    t, dt = 0, 1
    while(t < 10):
        x, y = ball.get_pos()
        turtle.goto(x, y)
        ball.move(dt)

    wn.mainloop()


if __name__ == '__main__':
    main()
