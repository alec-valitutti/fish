## Fish.py

## 2022-01-07

 

from typing import NamedTuple

import pygame,ctypes,random,Font

 

from pygame import font

 

user32 = ctypes.windll.user32

SCR_WID, SCR_HEI = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

 

class fish(pygame.sprite.Sprite):

    Name=''

    speed = 0

    facing = 'right'

    namePlate = pygame.Surface((32,32))

    def  __init__(self, name,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('../Assets/Images/fish.png').convert_alpha()

        self.image = pygame.transform.scale(self.image,(100,100))

        self.rect = self.image.get_rect()

        self.Name = name

        self.rect.x = x

        self.rect.y = y

        self.speed = random.randint(1,6)

        Font.textWrite(self.Name,Font.textFont,(255,255,255),self.image,0,0)

        self.namePlate.fill((50,50,50))

 

    def update(self):

        if self.rect.x <= SCR_WID and self.facing=='right':

            self.rect.x +=(1*self.speed)

            self.facing = 'right'

        else:

            self.rect.x -=(1*self.speed)

            self.facing = 'left'

        if self.rect.x <= -20:

            self.setSpeed()

            self.facing = 'right'

            self.image = pygame.transform.flip(self.image,1,0)

        if self.rect.x >=(SCR_WID-10):

            self.image = pygame.transform.flip(self.image,1,0)

 

    def setSpeed(self):

        self.speed = random.randint(1,6)