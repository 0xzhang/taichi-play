import taichi as ti
from datetime import datetime

ti.init()

size = 512
clock_size = size // 3
scale = clock_size / size
pixels = ti.Vector.field(3, ti.f32, shape=(size, size))
center = ti.Vector([size // 2, size // 2])
gui_center = ti.Vector([0.5, 0.5])
PI = 3.141592653589


def go(gui, continuous=False):
    # get time
    now = datetime.now()
    microsecond = now.microsecond
    second = now.second
    minute = now.minute
    hour = now.hour

    # clock body
    gui.circle(gui_center, radius=clock_size * 1.05, color=0xA0522D)
    gui.circle(gui_center, radius=clock_size, color=0xDCDCDC)

    # 5 minute marks
    for i in range(0, 60):
        pos = ti.Vector([ti.sin(2 * PI * i / 60), ti.cos(2 * PI * i / 60)])
        end = pos * scale + 0.5
        if i % 5 != 0:
            start = pos * scale * 0.9 + 0.5
            gui.line(start, end, radius=1, color=0x000000)
        else:
            start = pos * scale * 0.85 + 0.5
            gui.line(start, end, radius=2, color=0x000000)

    if continuous == True:
        secs = ti.Vector([
            ti.sin(2 * PI * (second + microsecond / 1000000) / 60),
            ti.cos(2 * PI * (second + microsecond / 1000000) / 60)
        ])
        mins = ti.Vector([
            ti.sin(2 * PI * (minute + second / 60) / 60),
            ti.cos(2 * PI * (minute + second / 60) / 60)
        ])
        hors = ti.Vector([
            ti.sin(2 * PI * (hour + minute / 60) / 12),
            ti.cos(2 * PI * (hour + minute / 60) / 12)
        ])
    else:
        secs = ti.Vector(
            [ti.sin(2 * PI * second / 60),
             ti.cos(2 * PI * second / 60)])
        mins = ti.Vector(
            [ti.sin(2 * PI * minute / 60),
             ti.cos(2 * PI * minute / 60)])
        hors = ti.Vector(
            [ti.sin(2 * PI * hour / 12),
             ti.cos(2 * PI * hour / 12)])

    # seconds hand
    secs = secs * scale * 0.9 + 0.5
    gui.line(gui_center, secs, radius=2, color=0xB22222)
    # minutes hand
    mins = mins * scale * 0.7 + 0.5
    gui.line(gui_center, mins, radius=3, color=0x000000)
    # hours hand
    hors = hors * scale * 0.4 + 0.5
    gui.line(gui_center, hors, radius=4, color=0x000000)

    # center mini circle
    gui.circle(gui_center, radius=clock_size * 0.06, color=0x000000)
    gui.circle(gui_center, radius=clock_size * 0.04, color=0xC0C0C0)


gui = ti.GUI("Canvas", res=(size, size), background_color=0x112F41)
continuous = False
switch = gui.button('switch')

while gui.running:
    for e in gui.get_events():
        if e.key == ti.GUI.ESCAPE:
            exit()
        elif e.key == switch:
            continuous = not continuous

    go(gui, continuous)
    gui.show()
