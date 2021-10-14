import taichi as ti
from solar_system import SolarSystem, Sun, Planet
from datetime import datetime, timedelta

ti.init(arch=ti.gpu)


def init_solarsystem():
    sun = Sun(0.2)
    ss = SolarSystem(sun)
    sun.initialize(ti.Vector([1, 0, 0]))

    # 2018-01-01
    ss.date = datetime.strptime("2018-01-01", '%Y-%m-%d').date()

    mercury = Planet(0.03)
    pos = ti.Vector(
        [-0.3877081979511674, -0.0077847346908167, 0.03493213369519331])
    vel = ti.Vector(
        [-0.005288319535531131, -0.02691956351115996, -0.001714528496530611])
    mercury.initialize(ti.Vector([1, 1, 1]), pos, vel)
    ss.add_planet(mercury)

    venus = Planet(0.1)
    pos = ti.Vector(
        [0.0711289554079218, -0.7236895081570862, -0.01403169883793853])
    vel = ti.Vector(
        [0.01999285129672666, 0.001906111736867988, -0.001127570469009755])
    venus.initialize(ti.Vector([1, 1, 0]), pos, vel)
    ss.add_planet(venus)

    earth = Planet(0.1)
    pos = ti.Vector(
        [-0.1752173047680441, 0.9675921579569661, -4.003213272786273e-05])
    vel = ti.Vector(
        [-0.01720893715482063, -0.003129664035086283, 1.997298538006543e-07])
    earth.initialize(ti.Vector([0, 1, 2]), pos, vel)
    ss.add_planet(earth)

    mars = Planet(0.06)
    pos = ti.Vector(
        [-1.583672712003512, -0.389028323418006, 0.03071411326349248])
    vel = ti.Vector(
        [0.003860856732981549, -0.01239426308040891, -0.0003544723155743041])
    mars.initialize(ti.Vector([2, 1, 0]), pos, vel)
    ss.add_planet(mars)

    return ss


def main():
    ss = init_solarsystem()

    window = ti.ui.Window('Solar System', (800, 600), vsync=True)
    canvas = window.get_canvas()
    scene = ti.ui.Scene()
    camera = ti.ui.make_camera()

    camera.position(0.0, -10.0, 5.0)
    camera.lookat(0.0, 0.0, 0.0)
    camera.fov(20)

    id_frame = 0
    pause_flag = True
    print("Press SPACE start move.")
    while window.running:
        window.GUI.begin("Statistics", 0.03, 0.05, 0.2, 0.12)
        window.GUI.text("Date: " + ss.get_date())
        window.GUI.text("Frame: " + str(id_frame))
        window.GUI.end()

        for e in window.get_events(ti.ui.PRESS):
            if e.key == ti.ui.ESCAPE:
                exit()
            elif e.key == ti.ui.SPACE:
                pause_flag = not pause_flag

        if not pause_flag:
            id_frame += 1
            ss.update(0.1)

        scene.set_camera(camera)
        ss.display(scene)
        scene.point_light(pos=(0.0, -5.0, 5.0), color=(0.5, 0.5, 0.5))
        canvas.scene(scene)
        window.show()


if __name__ == "__main__":
    main()