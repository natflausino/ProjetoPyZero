import pgzrun
import random

WIDTH = 800
HEIGHT = 600

floor_color = (105, 72, 30)


fly = Actor('enemy/fly_a.png')
fly.x = 900
fly.y = 80
fly.images = ['enemy/fly_a.png', 'enemy/fly_b.png']

slime = Actor('enemy/slime_fire_walk_b.png')
slime.x = 900
slime.y = 370
slime.images = ['enemy/slime_fire_walk_a.png', 'enemy/slime_fire_walk_b.png']


alien = Actor('character/alien_a.png')
alien.x = 100
alien.y = 370
alien.images = ['character/alien_a.png', 'character/alien_b.png']

vel_jump = 0
gravity = 1

def update():
    global vel_jump
    global gravity

    if keyboard.up:
        vel_jump = -10
    alien.y = alien.y + vel_jump
    vel_jump += gravity

    if alien.y > 370:
        vel_jump = 0
        alien.y > 370
    if alien.y < 0:
        vel_jump = 0
        alien.y = 0

    fly.x -= 4
    if fly.x < -10:
        fly.x = random.randint(1000, 2500)

    slime.x -= 3
    if slime.x < -15:
        slime.x = random.randint(1000, 2500)



def draw():
    screen.clear()

    background = images.background.background
    bg_width = background.get_width()

    cols = WIDTH // bg_width + 1

    for x in range(cols):
        screen.blit(background, (x * bg_width, 200))


    screen.draw.filled_rect(Rect(0,400,800, 600), (floor_color))
    screen.draw.filled_rect(Rect(0,0,800, 200), (255,255,255))

    fly.draw()
    slime.draw()
    alien.draw()

pgzrun.go()