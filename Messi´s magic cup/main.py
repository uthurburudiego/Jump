#Import libraries
import pygame
import random
from utilities import import_img
from Class_Player import Player
from Class_Platformer import Platform


#Initialise pygame
pygame.init()

#Game window dimensions
HEIGHT = 600
WIDTH = 400

#Set frame rate
clock = pygame.time.Clock()
FPS = 60 
#Maximum platforms
MAX_PLATFORMS = 10

#Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Messi Magic Cup")

#Load background
background_image = import_img("Messi´s magic cup/img/fondoestadio.jpg", WIDTH, HEIGHT)

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


#Create player
messi = Player(WIDTH // 2, HEIGHT - 150, screen)

#Create sprite groups
platform_group = pygame.sprite.Group()

#Create temporary platforms
for p in range(MAX_PLATFORMS):
    platform_width = random.randint(40, 60)
    platform_x = random.randint(0, WIDTH)
    platform_y = p * random.randint(80, 120)

    platform = Platform(platform_x, platform_y, platform_width, screen)
    platform_group.add(platform)


    if platform.rect.collidedict()


#Game loop
run = True
while run:

    clock.tick(FPS)

    messi.move(platform_group)

    #draw background
    screen.blit(background_image, (0, 0))

    #draw sprites
    messi.draw()
    platform_group.draw(screen)

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()    
    
pygame.quit()
