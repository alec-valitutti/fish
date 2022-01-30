import pygame.font

 



pygame.font.init()

textFont = pygame.font.Font('..\\Assets\\Fonts\\Ubuntu-Medium.ttf',16)
 

def textWrite(text,font,color,surface,x,y):

    textobj = font.render(text,1,color)

    textrect = textobj.get_rect()

    textrect.topleft = (x,y)

    surface.blit(textobj,textrect)