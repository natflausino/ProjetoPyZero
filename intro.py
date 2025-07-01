import pgzrun
import random
from pgzero import music

WIDTH = 800
HEIGHT = 600

floor_color = (105, 72, 30)
black = (0, 0, 0)

score = 0
life = 3
can_collide = True
play = False
music_on = True
music_started = False


button_play = Actor('icon/play.png', (400, 300))
button_exit = Actor('icon/exit.png', (500, 300))
button_music = Actor('icon/music_on.png', (300, 300))
button_music_off = Actor('icon/music_off.png', (300, 300))



fly = Actor('enemy/fly_a.png')
fly.x = 900
fly.y = 80
fly.images = ['enemy/fly_a.png', 'enemy/fly_b.png']

bee = Actor('enemy/bee_a.png')
bee.x = 900
bee.y = 80
bee.images = ['enemy/bee_a.png', 'enemy/bee_b.png']


slime = Actor('enemy/slime_fire_walk_b.png')
slime.x = 900
slime.y = 370
slime.images = ['enemy/slime_fire_walk_a.png', 'enemy/slime_fire_walk_b.png']


alien = Actor('character/alien_a.png')
alien.x = 100
alien.y = 370
alien.images = ['character/alien_a.png', 'character/alien_b.png']

hud_life = Actor('hud/hud_player_purple.png')
hud_life.x = 720
hud_life.y = 34

vel_jump = 0
gravity = 1

def hability_collide():
    global can_collide
    can_collide = True

def update():
    global vel_jump, gravity, score, life, can_collide
    global music_on, play, music_started

    if music_on and not music_started:
        music.play('musica')
        music.set_volume(0.8)
        music_started = True
    elif not music_on and music_started:
        music.stop()
        music_started = False

    if play:
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
            fly.y = random.randint(100, 260)

        bee.x -= 5
        if bee.x < -20:
            bee.x = random.randint(1000, 2600)
            bee.y = random.randint(100, 260)

        slime.x -= 3
        if slime.x < -15:
            slime.x = random.randint(1000, 2500)

        if (alien.colliderect(slime) or alien.colliderect(fly)) and can_collide:
            if music_on:
                sounds.sfx_disappear_fixed.play()
            life -= 1
            can_collide = False
            clock.schedule_unique(hability_collide, 3.0)

        if alien.colliderect(bee):
            if music_on:
                sounds.sfx_coin_fixed.play()
            bee.x = random.randint(1000, 2600)
            bee.y = random.randint(100, 260)
            score += 10


def draw_game_over(cols, bg_width):
    for x in range(cols):
        screen.blit(images.background.background_fade_mushrooms, (x * bg_width, 200))
    screen.draw.filled_rect(Rect(0,400,800, 600), (floor_color))
    screen.draw.text('Game Over', centerx=380, centery=150 , color=(black), fontname = 'alien_mushroom', fontsize = 100)
    screen.draw.text('Score: ' + str(score), centerx=380, centery=250, color=(black), fontname = 'alien_mushroom', fontsize = 50)

def draw_menu(cols, bg_width):
    for x in range(cols):
        screen.blit(images.background.background, (x * bg_width, 200))
    screen.draw.filled_rect(Rect(0,400,800, 600), (floor_color))
    screen.draw.text('Alien', centerx=380, centery=100 , color=(black), fontname = 'alien_mushroom', fontsize = 100)
    screen.draw.text('in ', centerx=380, centery=140 , color=(black), fontname = 'alien_mushroom', fontsize = 50)
    screen.draw.text('Mushrooms World', centerx=400, centery=175 , color=(black), fontname = 'alien_mushroom', fontsize = 100)
    button_play.draw()
    button_exit.draw()
    if music_on:
        button_music.draw()
    else:
        button_music_off.draw()


def on_mouse_down(pos):
    global play, music_on
    if  not play and button_play.collidepoint(pos):
        play = True
    elif music_on and button_music.collidepoint(pos):
        music_on = False
    elif not music_on and button_music_off.collidepoint(pos):
        music_on = True
    elif button_exit.collidepoint(pos):
        exit()

def draw():
    screen.clear()
    screen.draw.filled_rect(Rect(0,0,800, 200), (255,255,255))

    background = images.background.background
    bg_width = background.get_width()

    cols = WIDTH // bg_width + 1

    if play:
        if life == 0:
            draw_game_over(cols, bg_width)

        else:
            for x in range(cols):
                screen.blit(background, (x * bg_width, 200))
            screen.draw.filled_rect(Rect(0,400,800, 600), (floor_color))
            screen.draw.text('Score: ' + str(score), (20, 20), color=(black), fontname = 'alien_mushroom', fontsize = 50)
            screen.draw.text(str(life), (750, 20), color=(black), fontname = 'alien_mushroom', fontsize = 50)

            fly.draw()
            slime.draw()
            alien.draw()
            bee.draw()
            hud_life.draw()

    else:
        draw_menu(cols, bg_width)

pgzrun.go()