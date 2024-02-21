import pygame
from utilities import import_img

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, screen: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = import_img("Messi´s magic cup/img/plataforma pasto/4.png", width , 10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



