import pygame
from pygame.locals import QUIT, K_UP, K_DOWN, K_RIGHT, K_LEFT

def update():
    pygame.display.update()

def make_display(size, color):
    scr = pygame.display.set_mode(size)
    scr.fill(color.rgb_color)
    return scr

def make_group():
    return pygame.sprite.Group()


class SpriteBuilder(object):
    def __init__(self, sprite):
        self.sprt = sprite

    def __call__(self, *args, **kwargs):
        return self.sprt(*args,**kwargs)
