from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


pointx = [203, 132, 535, 477, 715, 316, 510, 692, 682, 712]
pointy = [535, 234, 470, 203, 136, 225, 92, 518, 336, 349]
num = 0


def next_direction(num1, num2):
    x = pointx[num2] - pointx[num1]
    y = pointy[num2] - pointy[num1]
    return x, y

def picture_direction(x, y, movex, frame):
        if (movex > 0):
            character.clip_draw(100 * frame, 100, 100, 100, x, y)
        if (movex < 0):
            character.clip_draw(100 * frame, 0, 100, 100, x, y)

def go_next_point(num1, num2):
    x = pointx[num1]
    y = pointy[num1]
    i = 0
    frame = 0
    movex, movey = next_direction(num1, num2)
    movex = movex // 10.0
    movey = movey // 10.0
    while i < 10:
        clear_canvas()
        grass.draw(400, 30)
        picture_direction(x, y, movex, frame)
        frame = (frame + 1) % 8
        update_canvas()
        x += movex
        y += movey
        i += 1
        delay(0.05)

while True:
    if(num < 9):
        go_next_point(num, num + 1)
        num += 1
    if(num == 9):
        go_next_point(num, 0)
        num = 0

close_canvas()

