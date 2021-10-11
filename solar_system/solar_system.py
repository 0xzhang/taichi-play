import taichi as ti
from datetime import datetime, timedelta


@ti.data_oriented
class CelestialObject:
    def __init__(self, radius, dim=3):
        self.radius = radius
        self.dim = dim
        self.color = ti.Vector.field(dim, ti.f32, shape=1)
        self.pos = ti.Vector.field(dim, ti.f32, shape=1)
        self.vel = ti.Vector.field(dim, ti.f32, shape=1)

    @ti.kernel
    def initialize(self, pos: ti.template(), vel: ti.template(),
                   color: ti.template()):
        self.pos[0] = pos
        self.vel[0] = vel
        self.color[0] = color

    def display(self, scene):
        scene.particles(self.pos, self.radius, per_vertex_color=self.color)


@ti.data_oriented
class Sun(CelestialObject):
    @ti.kernel
    def initialize(self, color: ti.template()):
        self.pos[0].fill(0.0)
        self.vel[0].fill(0.0)
        self.color[0] = ti.Vector([1.0, 0.0, 0.0])


@ti.data_oriented
class Planet(CelestialObject):
    @ti.kernel
    def update(self, dt: ti.f32):
        self.pos[0] += self.vel[0] * dt
        sqr_sum = self.pos[0].norm_sqr()
        # in units of AU/day^2
        acc = -2.959e-4 * self.pos[0] / sqr_sum**(3. / 2)
        self.vel[0] += acc * dt


@ti.data_oriented
class SolarSystem:
    def __init__(self, sun):
        self.sun = sun
        self.planets = []
        self.time = None

    def add_planet(self, planet):
        self.planets.append(planet)

    def update(self, dt=1):
        # self.time += timedelta(dt)
        for i, p in enumerate(self.planets):
            p.update(dt)

    def display(self, scene):
        self.sun.display(scene)
        for p in self.planets:
            p.display(scene)
