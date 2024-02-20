import pygame
from utilities import player_movements

WHITE = (255,255,255)
GRAVITY = 1

class Player():
    def __init__(self, x, y, screen: pygame.Surface) -> None:
        #Graphics
        self.animations = player_movements()
        self.animation = "still"
        self.image = self.animations[self.animation][0]
        self.jump = False
        self.screen = screen
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.velocity_y = 0

    def move(self):

        delta_x = 0
        delta_y = 0

        #Process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.animation = "left"
            delta_x =  -10
        elif key[pygame.K_d]:
            delta_x = 10
            self.animation = "right"
        elif not self.jump:
            self.animation = "still"

        #Gravity
        self.velocity_y += GRAVITY
        delta_y+= self.velocity_y

        #Secure player limits
        if self.rect.left + delta_x < 0:
            delta_x = -self.rect.left
        elif self.rect.right + delta_x > self.screen.get_width():
            delta_x =  self.screen.get_width() - self.rect.right
        if self.rect.bottom + delta_y-5 > self.screen.get_height():
            delta_y = 0
            self.velocity_y = -20


        #Update rectangle position 
        self.rect.x += delta_x
        self.rect.y += delta_y


    def draw(self):
        self.screen.blit(self.animations[self.animation][0], (self.rect.x -12, self.rect.y -10))
        pygame.draw.rect(self.screen, WHITE, self.rect, 2)
