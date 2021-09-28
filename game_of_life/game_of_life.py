import taichi as ti

ti.init(arch=ti.gpu)

N = 128
# How many pixels do you want to represent one cell?
M = 3*N

live_ratio = 0.6
cells = ti.field(ti.i32, shape=(N, N))
new_cells = ti.field(ti.i32, shape=(N, N))
pixels = ti.field(ti.f32, shape=(M, M))


@ti.kernel
def init_random():
    for i, j in cells:
        val = ti.random()
        if(val < live_ratio):
            cells[i, j] = 1


@ti.kernel
def init_blinker():
    step = 5
    iters = N/step
    for i in range(0, iters):
        for j in range(0, iters):
            cells[step*i + 1, step*j+2] = 1
            cells[step*i + 2, step*j+2] = 1
            cells[step*i + 3, step*j+2] = 1


@ti.kernel
def init_beacon():
    step = 6
    iters = N/step
    for i in range(0, iters):
        for j in range(0, iters):
            cells[step*i + 1, step*j+3] = 1
            cells[step*i + 2, step*j+4] = 1
            cells[step*i + 1, step*j+4] = 1
            cells[step*i + 3, step*j+1] = 1
            cells[step*i + 4, step*j+1] = 1
            cells[step*i + 4, step*j+2] = 1


@ti.kernel
def init_glider():
    cells[0, N-2] = 1
    cells[1, N-3] = 1
    cells[2, N-1] = 1
    cells[2, N-2] = 1
    cells[2, N-3] = 1


@ti.kernel
def evolve():
    for i, j in cells:
        new_cells[i, j] = cells[i, j]

    neighbors = 0
    for i, j in cells:
        neighbors = (cells[(i-1) % N, (j-1) % N] + cells[i, (j-1) % N]
                     + cells[(i+1) % N, (j-1) % N] + cells[(i-1) % N, j]
                     + cells[(i+1) % N, j] + cells[(i-1) % N, (j+1) % N]
                     + cells[i, (j+1) % N] + cells[(i+1) % N, (j+1) % N])
        if cells[i, j] == 1:
            if (neighbors < 2) or (neighbors > 3):
                new_cells[i, j] = 0
        else:
            if neighbors == 3:
                new_cells[i, j] = 1

    for i, j in cells:
        cells[i, j] = new_cells[i, j]


@ti.kernel
def zoom_in():
    scale = N/M
    for i, j in pixels:
        pixels[i, j] = cells[int(i*scale), int(j*scale)]


gui = ti.GUI("Game of Life", res=(M, M))

# init_random()
# init_blinker()
# init_beacon()
init_glider()

while gui.running:
    evolve()
    zoom_in()
    gui.set_image(pixels)
    gui.show()

# Export to pngs and convert to mp4/gif.
# ti video -f 50
# ti gif -i video.mp4
# for i in range(300):
#     evolve()
#     zoom_in()
#     gui.set_image(pixels)
#     filename = f'frame_{i:05d}.png'
#     print(f'Frame {i} is recorded in {filename}')
#     gui.show(filename)
