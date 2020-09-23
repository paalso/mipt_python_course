# Физическое моделирование материальной точки
# http://cs.mipt.ru/python/lessons/lab3.html#id16

import turtle
import math, time
import turtle_helper
import particle, vector


def max_flight_range(v0, alpha, a):
    return v0 * v0 / a * math.sin(2 * math.radians(alpha))


def main():
    # Инициализация графики
    BACKGROUND_COLOR = "lightblue"
    WIDTH, HEIGHT = 1200, 900
    wn = turtle_helper.make_window(
            BACKGROUND_COLOR, "Cannon shooting", WIDTH, HEIGHT)
    turtle = turtle_helper.make_turtle("blue", 0, 0, shape="circle")
    turtle.speed(9)
    turtle_helper.draw_line(0, 0, 1000, 0, "brown", 2, "arrow")

    text_output_pos = (3 / 5) * WIDTH, (4 / 5) * HEIGHT     # не пригодилось

    # Инициализация механики
    v0, alpha = 100, 80         # Эталон: v0, alpha = 100, 80
    p = vector.Vector(0, 0)
    v = vector.Vector( v0 * math.cos(math.radians(alpha)),
                v0 * math.sin(math.radians(alpha)))
    a = vector.Vector(0, -10)
    floor_vector = vector.Vector(1, 0)
    dissipation_quot = 0.4

    def is_collision(ball):
        _, y = ball.get_pos().coords()
        _, vy = ball.get_vel().coords()
        return y <= 0.1 and vy < 0

    def correct_pos(ball):
        ball.set_pos(vector.Vector(x, 0.000))

    def potential_energy(ball):
        x, y = ball.get_pos().coords()
        return 10 * y * ball.get_mass()

    ball = particle.Particle(p, v, a, potential_energy)

    t, moves, fps = 0, 0, 10
    dt = 1 / fps

    while(True):
        x, y = ball.get_pos().coords()
        # нужно задать некие разумные условия для остановки
        # они (первая часть - energy) зависят от fps, вернее от dt:
        # ниже fps - тем грубее расчеты - тем выше пороговое значение energy
        # и связаны с особенностями моделирования - с дискретностью расчетов
        if (energy := ball.get_energy()) < 20 and y <= 0:
            break

        # Выводим информацию о движении на косноль
        print("time:{:.1f}   (pos, vel, acc) = ".format(t), end="")
        ball.print_сinematics_info()
        ball.print_energy_info(); print()

        # Выводим информацию о движении на экран
##        if moves % fps == 0:
##            print(moves)
##            textlines = ["Time: {:.1f}".format(t)]
##            turtle_helper.print_text(*text_output_pos, textlines)
##        Честно пытался сделать вывод о текущем информации о движении на экран
##        но здесь, в Turtle Graphics, это оказывается крайне неудобным -
##        вывод текстовой информации занимает слишком много времени и это
##        нарушает отрисовку основного движения, - в общем fail

        ball.move(dt)
        moves += 1
        turtle.goto(x, y)
        if is_collision(ball):
            print("COLLISION")
            ball.collide_surface(floor_vector, correct_pos, dissipation_quot)

        t += dt

    wn.mainloop()


if __name__ == '__main__':
    main()
