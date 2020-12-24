import operator


def is_number(x):
    if type(x) in [int, float]:
        return True
    return False


class Vector:
    def __init__(self, *coords):
        self.vector = coords

    def coords(self):
        return tuple(self.vector)

    def __str__(self):
        return "({})".format(", ".join(map(str, self.vector)))

    def get_coords(self):
        return self.coords

    def __eq__(self, other):
        return self.coords == other.get_coords()

    def __add__(self, other):
        return Vector(*map(operator.add, self.vector, other.coords()))

    def __eq__(self, other):
        return self.vector == other.coords()

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return Vector(*map(operator.sub, self.vector, other.coords()))

    def __rsub__(self, other):
        return other - self

    def __mul__(self, other):
        if is_number(other):
            return Vector(*map(lambda e: e * other, self.vector))
        elif isinstance(other, Vector):
            return sum(map(operator.mul, self.vector, other.coords()))

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (1 / other)

    def __rtruediv__(self, other):
        return self  / other

    def length(self):
        return (sum(map(lambda e: e * e, self.vector))) ** 0.5

    def zero_vector(self):
        return Vector(*[0 for _ in range(len(self.vector))])

    def print(self, acc=2):
        rounded = map(lambda e: str(round(e, 2)) , self.vector)
        print("{}".format(", ".join(rounded)))

    def dist(self, other):
        return (self - other).length()

    def is_close(self, other, eps):
        return self.dist(other) <= eps

    def normalize(self):
        return self / self.length()

    def orthonormalize(self):   # for 2-dimensions only
        x, y = self.vector
        orthogonal = Vector(-y, x)
        return orthogonal.normalize()

    def reflect(self, other):        # for 2-dimensions only
    # Отразить заданный вектор относительно other
        return (self * other.normalize()) * other.normalize() - \
                (self * other.orthonormalize()) * other.orthonormalize()

    @staticmethod
    def summa(vectors):
        try:
            _sum = vectors[0].zero_vector()
            for v in vectors:
                _sum += v
            return _sum
        except:
            raise ValueError
