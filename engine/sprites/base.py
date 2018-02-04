import pygame

class Square(pygame.sprite.Sprite):
    def __init__(self, size, pos, color):
        super(Square, self).__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color.rgb_color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
