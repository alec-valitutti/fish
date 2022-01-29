from typing import NamedTuple

import pygame, ctypes, Fish as f

 

user32 = ctypes.windll.user32

 

SCR_WID, SCR_HEI = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((SCR_WID,SCR_HEI))

pygame.display.set_caption("Fish")

 

clock = pygame.time.Clock()

FPS =60

 

####################################################################################

####################################################################################

class namePlate(pygame.sprite.Sprite):

    namePlate = pygame.Surface((100,32))

    def __init__(self, r,g,b):

        pygame.sprite.Sprite.__init__(self)

        self.color = (r,g,b)

        self.image = self.namePlate

        self.rect = self.image.get_rect()

        self.image.fill(self.color)

        

x=namePlate(100,0,200)

 

def game():

    screen.fill((0,100,0))

    screen.blit(x.image,(400,400))

    

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:

                ## Prolly wana call the pause menu here

                exit()

        if event.type ==pygame.QUIT:

            exit()

    pygame.display.flip()

    clock.tick(FPS)

 

def main():

    while True:

        game()

 

#main()