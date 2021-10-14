import taichi as ti
import numpy as np

ti.init(arch=ti.cpu)

N = 32
# How many pixels do you want to represent one cell?
M = 16

live_ratio = 0.6
cells = ti.field(ti.i32, shape=(N, N))
neighbors = ti.field(ti.i32, shape=(N, N))


@ti.kernel
def init_random():
    for I in ti.grouped(cells):
        val = ti.random()
        if (val < live_ratio):
            cells[I] = 1


@ti.kernel
def init_glider():
    assert N > 3
    cells[0, N - 2] = 1
    cells[1, N - 3] = 1
    cells[2, N - 1] = 1
    cells[2, N - 2] = 1
    cells[2, N - 3] = 1


@ti.kernel
def init_blinker():
    step = 5
    iters = N / step
    for i in range(0, iters):
        for j in range(0, iters):
            cells[step * i + 1, step * j + 2] = 1
            cells[step * i + 2, step * j + 2] = 1
            cells[step * i + 3, step * j + 2] = 1


@ti.kernel
def init_beacon():
    step = 6
    iters = N / step
    for i in range(0, iters):
        for j in range(0, iters):
            cells[step * i + 1, step * j + 3] = 1
            cells[step * i + 2, step * j + 4] = 1
            cells[step * i + 1, step * j + 4] = 1
            cells[step * i + 3, step * j + 1] = 1
            cells[step * i + 4, step * j + 1] = 1
            cells[step * i + 4, step * j + 2] = 1


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


def main():
    gui = ti.GUI("Game of Life", res=(M * N, M * N))

    # init_random()
    init_glider()
    # init_blinker()
    # init_beacon()

    while gui.running:
        evolve()

        # A handy method learned from `examples/simulation/game_of_life.py` for zoom in frame.
        gui.set_image(ti.imresize(cells, M * N).astype(np.uint8) * 255)
        gui.show()

    # Export to pngs and convert to mp4/gif.
    # for i in range(300):
    #     evolve()
    #     zoom_in()
    #     gui.set_image(pixels)
    #     filename = f'frame_{i:05d}.png'
    #     print(f'Frame {i} is recorded in {filename}')
    #     gui.show(filename)


if __name__ == '__main__':
    main()