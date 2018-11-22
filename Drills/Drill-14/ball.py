import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self, boy):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.y = random.randint(75 + 10, boy.bg.h - 20 - 10)
        self.x = random.randint(int((210 - 0)/(boy.bg.h) * (self.y)) + 10,
                                boy.bg.w - int((210 - 0) / (boy.bg.h) * (self.y)) - 10)
        self.fall_speed = 0

    def get_bb(self):
        cx = self.x - self.bg.window_left
        cy = self.y - self.bg.window_bottom
        return cx - 10, cy - 10, cx + 10, cy + 10

    def set_background(self, bg):
        self.bg = bg

    def draw(self):
        cx = self.x - self.bg.window_left
        cy = self.y - self.bg.window_bottom
        self.image.draw(cx, cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time