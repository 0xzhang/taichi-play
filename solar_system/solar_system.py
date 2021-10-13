import taichi as ti
from datetime import datetime, timedelta

# Length of Year
# Tricky: I use many small spheres(call `scene.particles()``)
# to represent the orbit of planets.
# If dt is too small, 8000 is not enough, the orbit will be an arc.
LOY = 8000


@ti.data_oriented
class CelestialObject:
    def __init__(self, radius, dim=3):
        self.radius = radius
        self.dim = dim
        self.color = ti.Vector.field(dim, ti.f32, shape=1)
        self.pos = ti.Vector.field(dim, ti.f32, shape=1)

    def display(self, scene):
        scene.particles(self.pos, self.radius, per_vertex_color=self.color)


@ti.data_oriented
class Sun(CelestialObject):
    @ti.kernel
    def initialize(self, color: ti.template()):
        self.color[0] = color
        self.pos[0].fill(0.0)


@ti.data_oriented
class Planet(CelestialObject):
    def __init__(self, radius, dim=3):
        super().__init__(radius)
        self.vel = ti.Vector.field(dim, ti.f32, shape=1)
        self.orbit = ti.Vector.field(dim, ti.f32, shape=LOY)
        self.orbit_colors = ti.Vector.field(dim, ti.f32, shape=LOY)
        self.orbit_radius = self.radius / 8

    @ti.kernel
    def initialize(self, color: ti.template(), pos: ti.template(),
                   vel: ti.template()):
        self.color[0] = color
        self.pos[0] = pos
        self.vel[0] = vel

        self.orbit[0] = pos
        for i in range(LOY):
            self.orbit_colors[i] = color

    @ti.kernel
    def update(self, dt: ti.f32, step: ti.i32):
        self.pos[0] += self.vel[0] * dt
        sqr_sum = self.pos[0].norm_sqr()
        # in units of AU/day^2
        acc = -2.959e-4 * self.pos[0] / sqr_sum**(3. / 2)
        self.vel[0] += acc * dt

        self.orbit[step % LOY] = self.pos[0]

    def ghost(self, scene):
        scene.particles(self.orbit,
                        self.orbit_radius,
                        per_vertex_color=self.orbit_colors)


@ti.data_oriented
class SolarSystem:
    def __init__(self, sun):
        self.sun = sun
        self.planets = []
        self.date = None
        self.step = 0
        self.time = 0.0

    def add_planet(self, planet):
        self.planets.append(planet)

    def update(self, dt=1):
        self.step = (self.step + 1) % LOY
        self.time += dt
        for i, p in enumerate(self.planets):
            p.update(dt, self.step)

    def display(self, scene):
        self.sun.display(scene)
        for p in self.planets:
            p.display(scene)
            p.ghost(scene)

    def get_date(self):
        date = self.date + timedelta(int(self.time))
        return date.isoformat()