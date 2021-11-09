import taichi as ti
import numpy as np

ti.init(arch=ti.cpu)

N = 64
# How many pixels do you want to represent one cell?
M = 8

live_ratio = 0.6
cells = ti.field(ti.i32, shape=(N, N))
neighbors = ti.field(ti.i32, shape=(N, N))


@ti.kernel
def init():
    for I in ti.grouped(cells):
        val = ti.random()
        if (val < live_ratio):
            cells[I] = 1


@ti.func
def count(i, j):
    neighbors[i, j] = (cells[i - 1, j - 1] + cells[i, j - 1] +
                       cells[i + 1, j - 1] + cells[i - 1, j] +
                       cells[i + 1, j] + cells[i - 1, j + 1] +
                       cells[i, j + 1] + cells[i + 1, j + 1])


@ti.kernel
def evolve():
    for i, j in cells:
        count(i, j)

    for I in ti.grouped(cells):
        if neighbors[I] < 2 or neighbors[I] > 3:
            cells[I] = 0
        else:
            if neighbors[I] == 3:
                cells[I] = 1


if __name__ == '__main__':
    gui = ti.GUI("Game of Life", res=(M * N, M * N))
    init()

    while gui.running:
    # for i in range(1000):
        evolve()
        # A handy method learned from "taichi examples: game_of_life" for zoom in the frame.
        gui.set_image(ti.imresize(cells, M * N).astype(np.uint8) * 255)
        # filename = f'frame_{i:05d}.png'
        # print(f'Frame {i} is recorded in {filename}')
        # gui.show(filename)
        gui.show()