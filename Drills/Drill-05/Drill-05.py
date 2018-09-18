from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_from_center_to_right():
    x, y = 800 // 2, 90
    while x < 800 - 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.clip_draw(0, 300, 100, 100, x, 90)
        update_canvas()
        x += 2
        delay(0.05)
        get_events()

def move_up():
    x, y = 800 - 25, 90
    while y < 600 - 50:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(0, 300, 100, 100, x, y)
        y += 2
        update_canvas()
        delay(0.05)
        get_events()
    pass

def move_left():
    x, y = 800 - 25, 600 - 50
    while x > 0 + 25:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(0, 200, 100, 100, x, y)
        x -= 2
        update_canvas()
        delay(0.05)
        get_events()

def move_down():
    x, y = 0 + 25, 600 - 50
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(0, 200, 100, 100, x, y)
        y -= 2
        update_canvas()
        delay(0.05)
        get_events()

def move_left_to_center():
    x, y = 0 + 25, 90
    while x < 800 // 2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(0, 300, 100, 100, x, y)
        x += 2
        update_canvas()
        delay(0.05)
        get_events()
    pass

def make_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()
    move_left_to_center()

def make_circle():
    cx, cy, r = 800 // 2, 600 // 2, (600-180) // 2
    degree = -90
    while degree < 270:
        radian = math.radians(degree)
        x = cx + r * math.cos(radian)
        y = cy + r * math.sin(radian)
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.clip_draw(0, 300, 100, 100, x, y)
        degree += 1
        update_canvas()
        delay(0.05)
        get_events()

while True:
    make_rectangle()
    make_circle()

close_canvas()

