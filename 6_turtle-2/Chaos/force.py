# Черепаха как объект
# http://cs.mipt.ru/python/lessons/lab3.html#id17

import math, time
import vector, particle, sized_particle


# сила, действующая на первую точку со стороны второй
def force_between_two_particles(sz_particle1 : sized_particle.SizedParticle,
                            sz_particle2 : sized_particle.SizedParticle ):

    K = 1           # F = -K * m1 * m2 / d^2

    force_disctance_quotient = 7  # коэффициент максмальной дальности действия
    close_quotient = 0.2          # коэффициент минимальной близости действия
    # последний необходим, когда частицы оказваются очень близко или
    # совпадают - чтобы сила взаимодействия не возрастала до бесконечности

    pos1 = sz_particle1.get_pos()
    m1 = sz_particle1.get_mass()
    r1 = sz_particle1.get_radius()
    pos2 = sz_particle2.get_pos()
    m2 = sz_particle2.get_mass()
    r2 = sz_particle1.get_radius()

    if pos1 == pos2: return pos1 * 0

    from_pos2_to_pos1 = pos1 - pos2     # вектор из pos2 в pos1
    distance = (from_pos2_to_pos1 * from_pos2_to_pos1) ** 0.50

    print(distance)

    force_direction = from_pos2_to_pos1.normalize()

    # расстояние, на к-м частицы перестают взаимодействовыать
    if distance > force_disctance_quotient * ((r1 + r2) / 2) or \
            distance < close_quotient * min(r1, r2):
        return force_direction * 0      # нулевой вектор

    force_value = K * m1 * m2 / (distance * distance)
    force = force_direction * force_value
    return force


# результирующая сила, действующая на точку со стороны точек в списке
def resultant_force(sz_particle : sized_particle.SizedParticle,
                    sz_particles):
    from functools import reduce
    from operator import add

    return reduce(add, map(lambda szp : force_between_two_particles(
                                sz_particle, szp), sz_particles))


# результирующая сила, как функция от точки
def resultant_force_by_many_points(sz_particles):
    def inner(sz_particle : sized_particle.SizedParticle):
        return resultant_force(sz_particle, sz_particles)

    return inner


def main():
    pos1 = vector.Vector(0, 0)
    vel1 = vector.Vector(0, 0)
    acc1 = vector.Vector(0, 0)
    radius1 = 1
    p1 = sized_particle.SizedParticle(pos1, vel1, acc1, radius1)

    pos2 = vector.Vector(3, 3)
    vel2 = vector.Vector(0, 0)
    acc2 = vector.Vector(0, 0)
    radius2 = 1
    p2 = sized_particle.SizedParticle(pos2, vel2, acc2, radius2)

    pos3 = vector.Vector(2, 0)
    pos3 = vector.Vector(20, 0)
    vel3 = vector.Vector(0, 0)
    acc3 = vector.Vector(0, 0)
    radius3 = 1
    p3 = sized_particle.SizedParticle(pos3, vel3, acc3, radius3)

    L = [p1, p2, p3]

    result = resultant_force_by_many_points(L)
    print(result)
    print(result is None)
    print(type(result))

    print(result(p2))


if __name__ == '__main__':
    main()
