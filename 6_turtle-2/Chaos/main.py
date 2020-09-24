# Черепаха как объект
# http://cs.mipt.ru/python/lessons/lab3.html#id17

import turtle
import math, time
import turtle_helper
import particle, vector


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
    N = 150  # количество частиц
    radius = 11
    possible_vel_range = 1, 10  # возможный диапазон (составляющих) скоростей
    molecules = []
    turtles = dict()
    for _ in range(N):
        while True:
            x = random.randrange(int(radius * 1.5), int(width - radius * 1.5))
            y = random.randrange(int(radius * 1.5), int(height - radius * 1.5))
            pos = vector.Vector(x, y)
            if not molecules:
                break

            print(molecules, molecules[0].get_pos(), "radius ", radius * 1.5)
            print(pos, molecules[0].get_pos().dist(pos))
            print(list(map(
                    lambda m: m.get_pos().dist(pos) <= radius * 1.5, molecules)))
            print(list(map(
                    lambda m: m.get_pos().dist(pos), molecules)))
            print()

            if all(map(lambda m: m.get_pos().dist(pos) > radius * 2.5, molecules)):
                print("Have to continue:")
                for e in map(
                        lambda m: m.get_pos().dist(pos) <= radius * 1.5, molecules):
                    print(e)
                break
        v_min, v_max = possible_vel_range
        vx = random.randrange(v_min, v_max)
        vy = random.randrange(v_min, v_max)
        vel = vector.Vector(vx, vy)
        acc = vector.Vector(0, 0)
        molecule = particle.Particle(pos, vel, acc)
        molecules.append(molecule)
        turtle = turtle_helper.make_turtle("blue", 1, x, y, "circle")
        turtles[molecule] = turtle
        # turtle_helper.move()


    while(True):
        pass

        wn.mainloop()


if __name__ == '__main__':
    main()
