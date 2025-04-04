import pygame as pg
from sys import exit

pg.mixer.init()
pg.init()

musics = ["lab_7/music/undertale_001. Once Upon a Time.mp3", "lab_7/music/undertale_015. sans..mp3", "lab_7/music/undertale_063. It's Raining Somewhere Else.mp3"]

playdm = 0
isplaying = False
lenz = len(musics)
key_pressed = {"left": False, "right": False, "space": False, "s": False}

def play_music():
    global isplaying
    pg.mixer.music.stop()
    pg.mixer.music.load(musics[playdm])
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.1)
    isplaying = True

def stop_music():
    global isplaying
    pg.mixer.music.stop()
    isplaying = False

def play_next():
    global playdm
    playdm = (playdm + 1) % lenz
    play_music()

def play_prev():
    global playdm
    playdm = (playdm - 1) % lenz
    play_music()

W, H = 400, 200
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Music Player")

font = pg.font.SysFont(None, 28)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((30, 30, 30))
   
    track_text = font.render(f"Music: {musics[playdm] if isplaying else ' '}", True, (200, 200, 200))
    screen.blit(track_text, (20, 80))

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and not key_pressed["left"]:
        play_prev()
        key_pressed["left"] = True
    elif not keys[pg.K_LEFT]:
        key_pressed["left"] = False

    if keys[pg.K_RIGHT] and not key_pressed["right"]:
        play_next()
        key_pressed["right"] = True
    elif not keys[pg.K_RIGHT]:
        key_pressed["right"] = False

    if keys[pg.K_SPACE] and not key_pressed["space"]:
        if isplaying:
            pg.mixer.music.pause()
            isplaying = False
        else:
            pg.mixer.music.unpause()
            isplaying = True
        key_pressed["space"] = True
    elif not keys[pg.K_SPACE]:
        key_pressed["space"] = False

    if keys[pg.K_s] and not key_pressed["s"]:
        stop_music()
        key_pressed["s"] = True
    elif not keys[pg.K_s]:
        key_pressed["s"] = False

    pg.display.update()

pg.quit()