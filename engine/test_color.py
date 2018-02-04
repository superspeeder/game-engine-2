from base_utils import Color
from shortcuts.base import update, make_display, make_group, SpriteBuilder, quit_conditional
from sprites.base import Square

import pygame
from pygame.locals import *

BACKGROUND_COLOR = Color(255,255,255)
RED = Color(255,0,0)


screen = make_display((800,800), BACKGROUND_COLOR)
all_draw = make_group()

square = SpriteBuilder(Square)



all_draw.add(square((32,32), (300,300), RED))

update()


while 1:
    for event in pygame.event.get():
        quit_conditional(event)
