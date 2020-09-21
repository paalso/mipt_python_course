import turtle
import math, time
import turtle_helper
import particle, vector


def check_near_borders(window, turtle):
    x_min, x_max = - wn.window_width() // 2, wn.window_width() // 2
    y_min, y_max = - wn.window_height() // 2, wn.window_height() // 2
    x, y = turtle.xcor(), turtle.ycor()


def max_flight_range(v0, alpha, a):
    return v0 * v0 / a * math.sin(2 * math.radians(alpha))


def main():
    v0, alpha = 50, 85
##    print(max_flight_range(v0, alpha, 10))

    p = vector.Vector(0, 0)
    v = vector.Vector( v0 * math.cos(math.radians(alpha)),
                v0 * math.sin(math.radians(alpha)))
    a = vector.Vector(0, -10)
    ball = particle.Particle(p, v, a)
    floor_vector = vector.Vector(1, 0)
    dissipation_quot = 0.4

    def is_collision(ball):
        x, y = ball.get_pos().coords()
        vx, vy = ball.get_vel().coords()
        return y <= 0.1 and vy < 0

    def correct_pos(ball):
        ball.set_pos(vector.Vector(x, 0.000))

    def potential_energy(vector, mass):
        x, y = vector.coords()
        return 10 * y * mass

    print(ball)
    ball.print_сinematics_info()

    wn = turtle_helper.make_window("lightgreen", "Cannon shooting")
    wn.setworldcoordinates(0, 0, 1000, 850)
    turtle = turtle_helper.make_turtle("blue", 0, 0, shape="circle")
    turtle.speed(9)

##    x_min, x_max = - wn.window_width() // 2, wn.window_width() // 2
##    y_min, y_max = - wn.window_height() // 2, wn.window_height() // 2
    t, dt = 0, 0.05

    while(t < 1000):
        x, y = ball.get_pos().coords()
        if (energy := ball.get_energy(potential_energy)) < 10 and y <= 0:
            break
        print("time:{:.1f}  energy:{:.1f}   "
            .format(t, energy), end="")
        ball.print_сinematics_info()
        ball.print_energy_info()
        ball.move(dt)
        turtle.goto(x, y)
        if is_collision(ball):
            print("COLLISION")
            ball.collide_surface(floor_vector, correct_pos, dissipation_quot)

        t += dt

    wn.mainloop()


if __name__ == '__main__':
    main()
