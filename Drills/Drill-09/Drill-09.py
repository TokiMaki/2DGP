from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.bigimage = load_image('ball41x41.png')
        self.smallimage = load_image('ball21x21.png')
        self.speed = random.randint(5, 10)
        self.ballsize = random.randint(0, 1)
    def update(self):
        if (self.y - self.speed > 70 and self.ballsize == 0):
            self.y -= self.speed
        if (self.y - self.speed > 60 and self.ballsize == 1):
            self.y -= self.speed
        if (self.y - self.speed < 70 and self.ballsize == 0):
            self.y = 70
            self.speed = 0
        if (self.y - self.speed < 60 and self.ballsize == 1):
            self.y = 60
            self.speed = 0

    def draw(self):
        if (self.ballsize == 0):
            self.bigimage.clip_draw(0, 0, 41, 41, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
team = [Boy() for i in range(11)]
ball = [Ball() for i in range(20)]

running = True
# game main loop code
while running:
    handle_events()

    for boy in team:
        boy.update()

    for b in ball:
        b.update()

    clear_canvas()
    grass.draw()

    for boy in team:
        boy.draw()

    for b in ball:
        b.draw()

    update_canvas()
    delay(0.05)
# finalization code
close_canvas()