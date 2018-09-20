from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    global movex, movey
    global handx, handy
    global dir
    global motion
    global timer

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            handx, handy = event.x, KPU_HEIGHT - 1 - event.y
            movex, movey = go_point(x, y, event.x, KPU_HEIGHT - 1 - event.y)
            motion = draw_motion(movex)
            timer = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def go_point(characterx, charactery, pointx, pointy):
    movex = (pointx - characterx) // 10.0
    movey = (pointy - charactery) // 10.0
    return movex, movey

def draw_motion(movex):
    if movex > 0:
        return 1
    if movex < 0:
        return 0


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
movex = 0
movey = 0
timer = 0
frame = 0
motion = 0
handx, handy = 0, 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * motion, 100, 100, x, y)
    hand_arrow.draw(handx + 25, handy - 25)
    if (timer < 10):
        x += movex
        y += movey
        timer += 1
    frame = (frame + 1) % 8
    update_canvas()

    handle_events()
    delay(0.05)

close_canvas()

