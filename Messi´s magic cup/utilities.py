import pygame

def import_img(path: str, WIDTH, HEIGHT) -> pygame.Surface:
    
    return pygame.transform.scale( pygame.image.load(path), (WIDTH, HEIGHT))
