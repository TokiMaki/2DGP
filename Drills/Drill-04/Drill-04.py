from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
way = False
while (1):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    if (way == False):
        x = x + 2
    if (way == True):
        x = x - 2
    update_canvas()
    delay(0.01)
    if (x > 800):
        if (way == False):
                way = True
    if (x < 0):
        if (way == True):
            way = False


    get_events()

close_canvas()

