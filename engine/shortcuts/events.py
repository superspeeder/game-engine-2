import pygame
from pygame.locals import *


def quit_conditional(evt):
    if evt.type == QUIT:
        pygame.quit()
        exit()


def all_arrow_movement(sprt):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_LEFT]:
        sprt.move_left(3)
    if keys_pressed[K_RIGHT]:
        sprt.move_right(3)
    if keys_pressed[K_DOWN]:
        sprt.move_down(3)
    if keys_pressed[K_UP]:
        sprt.move_up(3)


def iskeypressed(event, key):
    if event.type == KEYDOWN:
        if event.key == key:
            return True

    return False