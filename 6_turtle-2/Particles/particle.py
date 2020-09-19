class Vector:
    def __init__(self, *coords):
        if len(coords) == 3:
            x, y, z = coords
            self.coords = {"x" : x, "y" : y, "z" : z}
        elif len(coords) == 2:
            x, y = coords
            self.coords = {"x" : x, "y" : y}
        elif len(coords) == 1:
            x = coords
            self.coords = {"x" : x}
        elif len(coords) == 0:
            self.coords = dict()

    def get_coords(self):
        return tuple(self.coords.values())

    def __str__(self, accuracy=2):

        if len(self.coords) == 2:
            x, y = self.coords["x"], self.coords["y"]
            return "({:.2f}, {:.2f})".format(x, y)
        elif len(self.coords) == 3:
            x, y, z = self.coords["x"], self.coords["y"], self.coords["z"]
            return f"({x}, {y}, {z})"

    def __mul__(self, number):
        new_values = map(lambda e: e * number, self.coords.values())
        return Vector(*new_values)

    def __truediv__(self, number):
        return self * (1 / number)


class Particle:
    def __init__(self, pos, vel, acc, mass=1):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def __str__(self):
        return "(mass: {}, position: {}, velocity: {}, acceleration: {})". \
            format(str(self.mass), str(self.pos), str(self.vel), str(self.acc))

    def get_pos(self):
        return self.pos.get_coords()

    def move(self, dt, F=None):
        new_pos = []
        new_vel = []
        for pos_coord, vel_coord, acc_coord in \
            zip(self.pos.coords.values(), self.vel.coords.values(), self.acc.coords.values()):
            new_pos.append(pos_coord + vel_coord * dt)
            new_vel.append(vel_coord + acc_coord * dt)
        self.pos = Vector(*new_pos)
        self.vel = Vector(*new_vel)

        if F:
            self.acc = F(self.pos, self.val) / self.mass

    def сinematics_info(self):
        s = str(self)
        return s[s.index("p"):]

    def print_сinematics_info(self):
        print(self.сinematics_info())
