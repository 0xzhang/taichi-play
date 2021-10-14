import taichi as ti
import numpy as np

ti.init(arch=ti.cpu)

N = 128
# How many pixels do you want to represent one cell?
M = 5

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
    neighbors[i,
              j] = (cells[(i - 1) % N, (j - 1) % N] + cells[i, (j - 1) % N] +
                    cells[(i + 1) % N, (j - 1) % N] + cells[(i - 1) % N, j] +
                    cells[(i + 1) % N, j] + cells[(i - 1) % N, (j + 1) % N] +
                    cells[i, (j + 1) % N] + cells[(i + 1) % N, (j + 1) % N])


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
        evolve()

        # A handy method learned from `examples/simulation/game_of_life.py` for zoom in frame.
        gui.set_image(ti.imresize(cells, M * N).astype(np.uint8) * 255)
        gui.show()