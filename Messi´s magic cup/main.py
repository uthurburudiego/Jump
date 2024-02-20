#Import libraries
import pygame
from utilities import import_img
from Class_Player import Player
#Initialise pygame
pygame.init()

#Game window dimensions
HEIGHT = 600
WIDTH = 400

#Set frame rate
clock = pygame.time.Clock()
FPS = 60 


#Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Messi Magic Cup")

#Load background
background_image = import_img("img/fondoestadio.jpg", WIDTH, HEIGHT)

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


#Create player
messi = Player(WIDTH // 2, HEIGHT - 150, screen)



#Game loop
run = True
while run:

    clock.tick(FPS)

    messi.move()

    #draw background
    screen.blit(background_image, (0, 0))

    #draw sprites
    messi.draw()

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()    
    
pygame.quit()
