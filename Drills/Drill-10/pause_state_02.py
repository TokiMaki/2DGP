import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state



name = "PauseState"
class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.frame = 0
    def update(self):
        self.frame = (self.frame + 1) % 10

    def draw(self):
        if (self.frame >= 5):
            self.image.clip_draw(0, 0, 900, 900, 400, 300, 300, 300)


pause = None
font = None

def enter():
    global pause
    pause = Pause()

def exit():
    global pause
    del(pause)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()


def update():
    pause.update()


def draw():
    clear_canvas()
    pause.draw()
    main_state.grass.draw()
    main_state.boy.draw()
    update_canvas()

