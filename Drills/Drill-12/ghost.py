from pico2d import *
import game_world
import random
import boy
import game_framework
import main_state
import math

class Ghost:
    image = None

    def __init__(self, x = 400, y = 300):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y = x, y
        self.frame = 0
        self.state = False
        self.rotate = 90
        self.r = 0
        self.x_cos = self.x
        self.y_sin = self.y
        self.font = load_font('ENCR10B.TTF', 16)
        boy.real_time = 0

    def draw(self):
        self.image.opacify(random.randint(1, 10) / 10.0)
        self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 3.141592 / 2, '', self.x_cos, self.y_sin, 100, 100)
