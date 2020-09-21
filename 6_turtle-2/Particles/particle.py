import vector

class Particle:
    def __init__(self, pos, vel, acc, mass=1):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.mass = mass

    def __str__(self):
        return "(mass: {}, position: {}, velocity: {}, acceleration: {})". \
            format(str(self.mass), str(self.pos), str(self.vel), str(self.acc))

    def get_pos(self):
        return self.pos

    def get_vel(self):
        return self.vel

    def get_acc(self):
        return self.acc

    def get_mass(self):
        return self.mass

    def set_pos(self, vector):
        self.pos = vector

    def set_vel(self, vector):
        self.vel = vector

    def set_acc(self, vector):
        self.acc = vector

    def get_kinetic_energy(self):
        return .5 * self.mass * self.vel * self.vel

    def get_energy(self, potential_energy=None):
        energy = self.get_kinetic_energy()
        if potential_energy:
            energy += potential_energy(self.pos, self.mass)
        return  energy

    def сinematics_info(self, accuracy=2):
        def round_collection(coll, accuracy):
            return tuple(map(lambda x: round(x, accuracy), coll))
        info = (self.pos.coords(), self.vel.coords(), self.acc.coords())
        return tuple(map(lambda t: round_collection(t, accuracy), info))

    def print_сinematics_info(self, accuracy=2):
        print(self.сinematics_info(accuracy), end=" ")

    def energy_info(self, accuracy=2):
        E, K = self.get_energy(), self.get_kinetic_energy()
        info = (E, K, E - K)
        return tuple(map(lambda t: round(t, accuracy), info))

    def print_energy_info(self, accuracy=2):
        print("Energy: {}, kinetic {}, potential {}".
            format(*self.energy_info()))

    def move(self, dt, F=None):
        self.pos = self.pos + self.vel * dt
        self.vel = self.vel + self.acc * dt
        if F:
            self.acc = F(self.pos, self.acc) / self.mass

    def dissipate(self, dissipate_quot):
        """
        Particle теряет часть кинетической энергии,
        E_new / E_old = 1 - dissipate_quot
        что проявляется в уменьшении скорости """

        self.vel = self.vel * (1 - dissipate_quot) ** 0.5

    def collide_surface(self, reflection_vector,
                        correct_pos=None, dissipate_quot=0):
        """
        При столкновении с поверхностью:
        - вектор скорости отражается относительно поверхности
        - возможно, корректируется положение
        - возможно, происходит дисипация энергии """
        self.vel = self.vel.reflect(reflection_vector)
        self.dissipate(dissipate_quot)
        if correct_pos:
            correct_pos(self)



(10.82, -63.82)
pos = vector.Vector(0, 10)
v = vector.Vector(0.564, -6.379)
a = vector.Vector(0, -10)
ball = Particle(pos, v, a)

def potential_energy(vector, mass=1):
    x, y = vector.coords()
    return 10 * y * mass


# print(ball.energy_info())
print()
"""

pos = vector.Vector(0, 0)
v = vector.Vector(0, 10)
a = vector.Vector(0, -10)
ball = Particle(pos, v, a)


def collision_condition(position):
    x, y = position.coords()
    return y <= 0

collision_vector = vector.Vector(1, 0)

t, dt = 0, 0.05

while t < 2.5:
    print("{:.1f}    {:.2f}".format(t, ball.get_energy(potential_energy)), end="  ")
    ball.print_сinematics_info()
    position = ball.get_pos()
    ball.move(dt)
    x, y = ball.get_pos().coords()
    if y <= 0:
        ball.print_сinematics_info()
        ball.collide_surface(collision_vector)
        print("COLLISION!")
        ball.set_pos(vector.Vector(x, 0))

    t += dt
"""