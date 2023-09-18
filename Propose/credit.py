import pygame as pg
import sys
from pygame.locals import *

pg.init()
pg.display.set_caption("Credits")

screen = pg.display.set_mode((640,480))
font = pg.font.Font("NanumGothic.ttf",32)
text = font.render("Hello, Pygame!", False, (255,255,255))
text_area = text.get_rect()
text_area.center = (320, 240)

while True:
    screen.blit(text,text_area)

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    pg.display.update()
