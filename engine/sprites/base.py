import pygame

class Square(pygame.sprite.Sprite):
    def __init__(self, size, pos, color):
        super(Square, self).__init__()
        self.capabilities = []
        self.image = pygame.Surface(size)
        self.image.fill(color.rgb_color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
    def add_capabilities(self, *capabilities):
        for capability in capabilities:
            if capability not in self.capabilities:
                self.capabilities.append(capability)

    def revoke_capabilities(self, *capabilities):
        for capability in capabilities:
            if capability in self.capabilities:
                del self.capabilities[self.capabilities.index(capability)]

    def toggle_capabilities(self, *capabilities):
        revoked = []
        added = []
        for capability in capabilities:
            if capability in self.capabilities:
                revoked.append(capability)
            else:
                added.append(capability)

        self.revoke_capabilities(*revoked)
        self.add_capabilities(*added)