from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
dir = 0
x1 = 400
y1 = 90
angle = 270
since = 1
clip = 0
pi = 3.141592 / 180.0

while (True):
        if since == 1:
                if dir == 0:
                    clear_canvas_now()
                    grass.draw_now(400,30)
                    character.draw_now(x,y)
                    x = x + 8
                    delay(0.01)
                    if x >= 400:
                            if clip == 1:
                                since = 0
                                dir = 0
                                clip = 0
                    if x >= 800:
                        dir = 1
                if dir == 1:
                    clear_canvas_now()
                    grass.draw_now(400,30)
                    character.draw_now(x,y)
                    y = y + 8
                    delay(0.01)
                    if y >= 600:
                        dir = 2
                if dir == 2:
                    clear_canvas_now()
                    grass.draw_now(400,30)
                    character.draw_now(x,y)
                    x = x - 8
                    delay(0.01)
                    if x <= 0:
                        dir = 3
                if dir == 3:
                    clear_canvas_now()
                    grass.draw_now(400,30)
                    character.draw_now(x,y)
                    y = y - 8
                    delay(0.01)
                    if y <= 90:
                        dir = 0
                        clip = 1

        if since == 0:
                clear_canvas_now()
                grass.draw_now(400,30)
                x1 = math.cos(angle * pi) * 255 + 400
                y1 = math.sin(angle * pi) * 255 + 255 + 90
                character.draw_now(x1,y1)
                angle = angle + 1
                delay(0.01)
                if angle >= 630:
                        angle = 270
                        x = 400
                        y = 90
                        since = 1


close_canvas()
