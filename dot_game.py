import pygame
pygame.font.init()
pygame.init()
HEIGHT = 600
WIDTH = 600
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Dot Game")
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen.fill(WHITE)
pygame.display.flip()

r = pygame.Rect((3,3), (100,200))
pygame.draw.rect(screen, WHITE, r)
pygame.display.flip()

screen.blit(font.render("{0}x{0}".format(sizeOfGrid), True, (10, 10, 10)), (32, 210))
