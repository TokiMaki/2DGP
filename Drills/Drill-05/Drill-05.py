from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

pointx = [203, 132, 535, 477, 715, 316, 510, 692, 682, 712]
pointy = [535, 234, 470, 203, 136, 225, 92, 518, 336, 349]

def next_direction(num1, num2):
    x = pointx[num2] - pointx[num1]
    y = pointy[num2] - pointy[num1]
    return x, y

def go_next_point(num1, num2):
    x = pointx[num1]
    y = pointy[num1]
    movex, movey = next_direction(num1, num2)
    pass

while True:
    go_next_point(num, num + 1)

close_canvas()

