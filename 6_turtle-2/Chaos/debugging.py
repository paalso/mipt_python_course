import vector
import particle
import main

p = particle.Particle(vector.Vector(0, 0), vector.Vector(0, 0), vector.Vector(0, 0))
p1 = particle.Particle(vector.Vector(1, 1), vector.Vector(0, 0), vector.Vector(0, 0), mass=2)
p2 = particle.Particle(vector.Vector(1, 0), vector.Vector(0, 0), vector.Vector(0, 0), mass=1)

# F = p.inverse_square_force(p1)
##F = main.inverse_square_force(p, p1)
##F.print()

v1 = vector.Vector(1,1)
v2 = vector.Vector(1,2,2)
v3 = vector.Vector(1,2,20)
vectors = []
print(v1 + v2 + v3)
print(vectors)
vectors_sum = vector.Vector.summa(vectors)
print(vectors_sum)
