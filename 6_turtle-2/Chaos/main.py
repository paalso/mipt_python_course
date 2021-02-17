# Черепаха как объект
# http://cs.mipt.ru/python/lessons/lab3.html#id17

import turtle
import math, time
import turtle_helper
import vector, particle, sized_particle


def walls_collision(sz_particle : sized_particle.SizedParticle,
        width, height):
    x, y = sz_particle.get_pos().coords()
    vx, vy = sz_particle.get_vel().coords()
    radius = sz_particle.get_radius()
    if x <= radius: return vector.Vector(0, 1)
    if x >= width - radius: return vector.Vector(0, -1)
    if y <= radius: return vector.Vector(-1, 0)
    if y >= height - radius: return vector.Vector(1, 0)


def inverse_square_force(particle, other, G=1):
    """
    Сила, действующая по закону обратных квадратов на particle
    со стороны other
    G - коэффициент - аналог Гравитационной постоянной """
    pos = particle.get_pos()     # радиус-вектор частицы particle
    other_pos = other.get_pos()  # радиус-вектор частицы other
    dist = pos.dist(other_pos)   # расстояние между ними

    # Нужно бы обработать ситуацию, когда внезапно векторы pos и other
    # или их координаты полностью совпадают, в этом случае сила
    # вообще то обращается в Inf, но пусть будет так:
    if pos == other_pos:
        return pos.zero_vector()

    pos_to_other = other_pos - pos  # вектор от частицы particle к other
    force = G * particle.get_mass() * other.get_mass() * pos_to_other \
            / dist ** 3
    return force


def main():
    # Инициализация графики
    BACKGROUND_COLOR = "lightblue"
    WIDTH, HEIGHT = 1000, 850
    wn = turtle_helper.make_window(
            BACKGROUND_COLOR, "Cannon shooting", WIDTH, HEIGHT)
    margin = 8
    width, height = WIDTH - margin, HEIGHT - margin

    # границы объема
    turtle_helper.draw_rectangle(0, 0, width, height, "brown", 2)

    # turtle_helper.move(particle, 100, 105)

    # Инициализация
    import random
    N = 25  # количество частиц
    radius = 11
    possible_vel_range = -100, 100  # диапазон (составляющих) скоростей
    molecules = []
    turtles = dict()
    for _ in range(N): # начальная расстановка 'молекул'

        while True: # обеспечиваем, чтобы они не липли к краям и друг к другу
            x = random.randrange(int(radius * 1.5), int(width - radius * 1.5))
            y = random.randrange(int(radius * 1.5), int(height - radius * 1.5))
            pos = vector.Vector(x, y)
            if not molecules: break     # первая молекла - без проверок
            if all(map(
                    lambda m: m.get_pos().dist(pos) > radius * 2.5, molecules)):
                break

        v_min, v_max = possible_vel_range
        vx, vy = random.randrange(v_min, v_max), random.randrange(v_min, v_max)
        vel = vector.Vector(vx, vy)
        acc = vector.Vector(0, 0)
        molecule = sized_particle.SizedParticle(pos, vel, acc, radius);
        molecules.append(molecule)
        turtle = turtle_helper.make_turtle("blue", 1, x, y, "circle")
        turtle.penup()
        turtle.speed(50)
        turtles[molecule] = turtle

    t, moves = 0, 0
    dt = 0.025
    G = -100000

    while(True):    # начинаем движение
        moves += 1
        t += dt
        for molecule in molecules:

            F = vector.Vector.summa(list(map(
                    lambda mol: inverse_square_force(molecule, mol, G),
                    molecules)))

            molecule.move(dt, F)
            x, y = molecule.get_pos().coords()

            # проверка на столкновения с границами
            if (v := walls_collision(molecule, width, height)):
                molecule.collide_surface(v)

            turtles[molecule].goto(x, y)

    wn.mainloop()


if __name__ == '__main__':
    main()