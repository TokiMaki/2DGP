from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
way = False
while (1):
    clear_canvas()
    grass.draw(400, 30)
    if (way == False):
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        x = x + 5
    if (way == True):
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        x = x - 5
    update_canvas()
    frame = (frame + 1) % 8
    if (x > 800):
        if (way == False):
                way = True
    if (x < 0):
        if (way == True):
            way = False
    delay(0.05)
    get_events()

close_canvas()

