import particle


class SizedParticle(particle.Particle):

    def __init__(self, pos, vel, acc, radius, potential_energy=None, mass=1):
        particle.Particle.__init__(self, pos, vel, acc, potential_energy, mass)
        self.radius = radius

    def get_radius(self):
        return self.radius
