import pygame

def import_img(path: str, WIDTH, HEIGHT) -> pygame.Surface:
    
    return pygame.transform.scale( pygame.image.load(path), (WIDTH, HEIGHT))

def player_movements():
    still = [ import_img("Messi´s magic cup\img\messi\quieto.png",45,72)]
    run = [ import_img("Messi´s magic cup\img\messi\corriendo.png",45,72)]
    right = [import_img("Messi´s magic cup\img\messi\costado.png",45,72)]
    left = [pygame.transform.flip(right[0], True, False)]
    back = [import_img("Messi´s magic cup\img\messi\espalda.png",45,72)]
    back_jump = [import_img("Messi´s magic cup\img\messi\espaldasalto.png",45,72)]
    jump = [import_img("Messi´s magic cup\img\messi\salto.png",45,72)]
    sitting = [import_img("Messi´s magic cup\img\messi\sentado.png",45,72)]

    return {
        'still':still,
        'run':run,
        'right':right,
        'left':left,
        'back':back,
        'back_jump':back_jump,
        'jump':jump,
        'sitting':sitting
    }