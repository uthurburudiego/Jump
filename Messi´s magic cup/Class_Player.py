import pygame
from utilities import import_img

WHITE = (255,255,255)

class Player():
    def __init__(self, x, y, screen: pygame.Surface) -> None:
        self.image = import_img("img\messi\quieto.png", 45, 72)
        self.screen = screen
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)

    def move(self):

        delta_x = 0
        delta_y = 0

        #Process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
           delta_x =  -10
        if key[pygame.K_d]:
           delta_x = 10
        if key[pygame.K_w]:
            pass
        if key[pygame.K_s]:
            pass

        #Secure player limits
        if self.rect.left + delta_x < 0:
            delta_x = -self.rect.left
        elif self.rect.right + delta_x > self.screen.get_width():
            delta_x =  self.screen.get_width() - self.rect.right
            print(self.rect.x)


        #Update rectangle position 
        self.rect.x += delta_x
        self.rect.y += delta_y


    def draw(self):
        self.screen.blit(self.image, (self.rect.x -12, self.rect.y -10))
        pygame.draw.rect(self.screen, WHITE, self.rect, 2)
