# Черепаха как объект
# http://cs.mipt.ru/python/lessons/lab3.html#id17

import turtle
import math, time
import turtle_helper
import vector, particle, sized_particle


def is_walls_collision(sz_particle : sized_particle.SizedParticle,
        width, height):
    x, y = sz_particle.get_pos().coords()
    vx, vy = sz_particle.get_vel().coords()
    radius = sz_particle.get_radius()
    return x <= radius or x + radius >= width or \
            y <= radius or y + radius >= height


def walls_collision(sz_particle : sized_particle.SizedParticle,
        width, height):
    x, y = sz_particle.get_pos().coords()
    vx, vy = sz_particle.get_vel().coords()
    radius = sz_particle.get_radius()
    if x <= radius: return vector.Vector(0, 1)
    if x >= width - radius: return vector.Vector(0, -1)
    if y <= radius: return vector.Vector(-1, 0)
    if y >= height - radius: return vector.Vector(1, 0)


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
    possible_vel_range = 1, 100  # возможный диапазон (составляющих) скоростей
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
        # molecule = particle.Particle(pos, vel, acc);
        molecule = sized_particle.SizedParticle(pos, vel, acc, radius);
        molecules.append(molecule)
        turtle = turtle_helper.make_turtle("blue", 1, x, y, "circle")
        turtle.penup(); turtle.speed(0)
        turtles[molecule] = turtle

    t, moves = 0, 0
    dt = 0.1

    while(True):    # начинаем движение
        moves += 1
        t += dt
        for molecule in molecules:
            molecule.move(dt)
            x, y = molecule.get_pos().coords()

            # проверка на столкновения с границами
            if (v := walls_collision(molecule, width, height)):
##                print(v)
                molecule.collide_surface(v)

            turtles[molecule].goto(x, y)

    wn.mainloop()


if __name__ == '__main__':
    main()
