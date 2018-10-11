import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state



name = "PauseState"

pause = None
font = None

def enter():
    global pause
    pause = load_image('pause.png')

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


def update():
    pass


def draw():
    clear_canvas()
    update_canvas()





