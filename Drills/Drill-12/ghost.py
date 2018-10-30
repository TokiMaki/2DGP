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

    def update(self):
        self.frame = (self.frame + boy.FRAMES_PER_ACTION * boy.ACTION_PER_TIME * game_framework.frame_time) % 8
        if (self.state == 0):
            self.r += boy.RUN_SPEED_PPS * game_framework.frame_time
            self.x_cos = self.x + math.cos(math.pi / 180 * self.rotate) * self.r
            self.y_sin = self.y + math.sin(math.pi / 180 * self.rotate) * self.r
            if (self.r >= 100):
                self.r = 100
                self.state = 1

        if (self.state == 1):
            boy.real_time += game_framework.frame_time
            self.rotate += 720 * game_framework.frame_time
            self.x_cos = self.x + math.cos(math.pi / 180 * self.rotate) * self.r
            self.y_sin = self.y + math.sin(math.pi / 180 * self.rotate) * self.r

        if (boy.real_time >= 1.0):
            boy.real_time = boy.real_time % 1

        if (main_state.boy.cur_state != boy.SleepState):
            game_world.remove_object(self)


