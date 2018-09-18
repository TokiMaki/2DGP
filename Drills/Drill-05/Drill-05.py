from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

pointx = [203, 132, 535, 477, 715, 316, 510, 692, 682, 712]
pointy = [535, 234, 470, 203, 136, 225, 92, 518, 336, 349]

def go_next_point():
    pass


while True:
    num = 0
    go_next_point()

close_canvas()

