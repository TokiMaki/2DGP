from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

global frame
global motion

def draw_line(p1, p2):
    frame = 0
    motion = 2
    for i in range(0, 100 + 1, 5):
        clear_canvas()
        t = i / 100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1-t)*p1[1]+t*p2[1]

size = 20
points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(size)]
n = 1

while True:
    draw_line(points[n - 1], points[n])
    n = (n + 1) % size

