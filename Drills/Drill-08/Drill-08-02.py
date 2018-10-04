from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

def draw_curve_4_points(p1, p2, p3, p4):
    frame = 0
    motion = 2
    clear_canvas()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH / 2, KPU_HEIGHT / 2)
        for j in range(0, 10, 1):
            character.clip_draw(0, 0, 100, 100, points[j][0], points[j][1])
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        if (p1[0] <= p2[0]):
            motion = 1
        if (p1[0] > p2[0]):
            motion = 0
        character.clip_draw(frame * 100, 100 * motion, 100, 100, x, y)
        frame = (frame + 1) % 8
        delay(0.05)
        update_canvas()

size = 10

points = [(random.randint(0, 1280), random.randint(0, 1024)) for i in range(size)]

n = 0

while True:
    draw_curve_4_points(points[(n) % 10], points[(n+1) % 10], points[(n+2) % 10], points[(n+3) % 10])
    n = (n + 1) % size


