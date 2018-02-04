import base_utils as util
from shortcuts.base import update, make_display, make_group, SpriteBuilder
from shortcuts.events import quit_conditional, all_arrow_movement, iskeypressed
from sprites.movables import MoveSquare
import pygame
from pygame.locals import *
BACKGROUND_COLOR = util.Color(255, 255, 255)
RED = util.Color(255, 0, 0)
screen = make_display((800, 800), BACKGROUND_COLOR)
all_draw = make_group()
square = SpriteBuilder(MoveSquare)
psquare = square((32, 32), (300, 300), RED)
all_draw.add(psquare)
all_draw.draw(screen)
update()
while 1:
    for event in pygame.event.get():
        quit_conditional(event)
        if iskeypressed(event, K_SPACE):
            psquare.toggle_capabilities("move_up")

    all_arrow_movement(psquare)
    screen.fill(BACKGROUND_COLOR.rgb_color)
    all_draw.draw(screen)
    update()