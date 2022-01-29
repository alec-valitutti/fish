import pygame.font

 



textFont = pygame.font.init()

 

def textWrite(text,font,color,surface,x,y):

    textobj = font.render(text,1,color)

    textrect = textobj.get_rect()

    textrect.topleft = (x,y)

    surface.blit(textobj,textrect)