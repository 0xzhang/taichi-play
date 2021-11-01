import taichi as ti
from datetime import datetime

ti.init()

x_width, y_width = 512, 512
scale = x_width / y_width
gui_center = ti.Vector([0.5, 0.5])
PI = 3.141592653589
digits = [[1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1],
          [1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 1, 0, 1, 1],
          [1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1]]
endpoint = 0.015
offsets = [[0.05, 0.4], [0.183, 0.4], [0.383, 0.4], [0.517, 0.4], [0.717, 0.4],
           [0.85, 0.4]]


def dots(gui, dot_color=0xED553B):
    x = 0.333
    y1 = 0.4 + 0.075 * scale
    y2 = 0.4 + 0.125 * scale
    gui.circle([x, y1], radius=5, color=dot_color)
    gui.circle([x, y2], radius=5, color=dot_color)
    x = 0.667
    gui.circle([x, y1], radius=5, color=dot_color)
    gui.circle([x, y2], radius=5, color=dot_color)


def segments(gui, masks=[1] * 7, offsets=offsets, seg_color=0x202020):
    xinc = 0.1
    yinc = 0.1 * scale
    for off in offsets:
        # 0
        if masks[0]:
            x = off[0] + 0.0
            y = off[1] + 0.2 * scale
            gui.line([x + endpoint, y], [x + xinc - endpoint, y],
                     radius=5,
                     color=seg_color)
        # 1
        if masks[1]:
            x = off[0] + 0.1
            y = off[1] + 0.1 * scale
            gui.line([x, y + endpoint], [x, y + yinc - endpoint],
                     radius=5,
                     color=seg_color)
        # 2
        if masks[2]:
            x = off[0] + 0.1
            y = off[1] + 0.0
            gui.line([x, y + endpoint], [x, y + yinc - endpoint],
                     radius=5,
                     color=seg_color)
        # 3
        if masks[3]:
            x = off[0] + 0.0
            y = off[1] + 0.0
            gui.line([x + endpoint, y], [x + xinc - endpoint, y],
                     radius=5,
                     color=seg_color)
        # 4
        if masks[4]:
            x = off[0] + 0.0
            y = off[1] + 0.0
            gui.line([x, y + endpoint], [x, y + yinc - endpoint],
                     radius=5,
                     color=seg_color)
        # 5
        if masks[5]:
            x = off[0] + 0.0
            y = off[1] + 0.1 * scale
            gui.line([x, y + endpoint], [x, y + yinc - endpoint],
                     radius=5,
                     color=seg_color)
        # 6
        if masks[6]:
            x = off[0] + 0.0
            y = off[1] + 0.1 * scale
            gui.line([x + endpoint, y], [x + xinc - endpoint, y],
                     radius=5,
                     color=seg_color)


def go(gui, format24=True):
    # get time
    now = datetime.now()
    microsecond = now.microsecond
    second = now.second
    minute = now.minute
    hour = now.hour
    if format24 is True:
        time = now.strftime("%H:%M:%S")
    else:
        time = now.strftime("%I:%M:%S")
    gui.text(time, [0.05, 0.95], 30)
    time = time.replace(':', '')
    for i in range(len(time)):
        idx = int(time[i])
        segments(gui, digits[idx], [offsets[i]], 0xED553B)


gui = ti.GUI("Digital Clock",
             res=(x_width, y_width),
             background_color=0x000000)
format24 = True
switch = gui.button('24/12')

for i in range(1800):
# while gui.running:
    for e in gui.get_events():
        if e.key == ti.GUI.ESCAPE:
            exit()
        elif e.key == switch:
            format24 = not format24

    segments(gui)
    dots(gui)
    go(gui, format24)
    # gui.show()

    if i%5 == 0:
        filename = f'frame_{i:05d}.png'
        print(f'Frame {i} is recorded in {filename}')
        gui.show(filename)
    else:
        gui.show()
