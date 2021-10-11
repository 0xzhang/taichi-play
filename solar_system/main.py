import taichi as ti
from solar_system import SolarSystem, Sun, Planet

ti.init(arch=ti.gpu)


def init_solarsystem():
    sun = Sun(0.2)
    ss = SolarSystem(sun)
    color = ti.Vector([1, 0, 0])
    sun.initialize(color)

    mercury = Planet(0.03)
    pos = ti.Vector(
        [-0.3877081979511674, -0.0077847346908167, 0.03493213369519331])
    vel = ti.Vector(
        [-0.005288319535531131, -0.02691956351115996, -0.001714528496530611])
    color = ti.Vector([1, 1, 1])
    mercury.initialize(pos, vel, color)
    ss.add_planet(mercury)

    venus = Planet(0.1)
    pos = ti.Vector(
        [0.0711289554079218, -0.7236895081570862, -0.01403169883793853])
    vel = ti.Vector(
        [0.01999285129672666, 0.001906111736867988, -0.001127570469009755])
    color = ti.Vector([1, 1, 0])
    venus.initialize(pos, vel, color)
    ss.add_planet(venus)

    earth = Planet(0.1)
    pos = ti.Vector(
        [-0.1752173047680441, 0.9675921579569661, -4.003213272786273e-05])
    vel = ti.Vector(
        [-0.01720893715482063, -0.003129664035086283, 1.997298538006543e-07])
    color = ti.Vector([0, 1, 2])
    earth.initialize(pos, vel, color)
    ss.add_planet(earth)

    mars = Planet(0.06)
    pos = ti.Vector(
        [-1.583672712003512, -0.389028323418006, 0.03071411326349248])
    vel = ti.Vector(
        [0.003860856732981549, -0.01239426308040891, -0.0003544723155743041])
    color = ti.Vector([2, 1, 0])
    mars.initialize(pos, vel, color)
    ss.add_planet(mars)

    return ss


def main():
    ss = init_solarsystem()

    window = ti.ui.Window('Solay system', (800, 800))
    canvas = window.get_canvas()
    scene = ti.ui.Scene()
    camera = ti.ui.make_camera()
    camera.position(0.0, 0.0, 5.0)
    camera.lookat(0.0, 0.0, 0.0)
    # camera.fov(80)

    while window.running:
        # step(0.001)
        ss.update(0.01)
        camera.track_user_inputs(window,
                                 movement_speed=0.03,
                                 hold_key=ti.ui.RMB)
        scene.set_camera(camera)
        ss.display(scene)
        scene.point_light(pos=(0.5, 1.5, 1.5), color=(0.5, 0.5, 0.5))
        canvas.scene(scene)
        window.show()


if __name__ == "__main__":
    main()