##fish.py

##Alec valitutti

##2022-01-07

 

##################################################

 

import pygame, ctypes, Fish as f

 

user32 = ctypes.windll.user32

 

SCR_WID, SCR_HEI = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((SCR_WID,SCR_HEI))

pygame.display.set_caption("Fish")

 

clock = pygame.time.Clock()

FPS =60

 

# pygame.mixer.init(48000,16,2,4096)

 

# pygame.mixer.set_num_channels(24)

fishgroup = pygame.sprite.Group(())

 

Alec = f.fish("Alec",0,0)

Apurva = f.fish("Apurva",200,50)

Ashley = f.fish("Ashley",100,500)

Katie = f.fish("Katie",50,300)

Nisha = f.fish("Nisha",60,200)

Nimit = f.fish("Nimit",30,630)

Stephanie = f.fish("Stepahnie",200,100)

Shannon = f.fish("Shannon",40,450)

Ben = f.fish("Ben", 400,600)

Paige = f.fish("Paige", 200,700)

Natalie = f.fish("Natalie", 350,1000)

Elise = f.fish("Elise",1200,400)

Nick = f.fish("Nick",800,500)

 

fishgroup.add(Alec)

fishgroup.add(Apurva)

fishgroup.add(Ashley)

fishgroup.add(Katie)

fishgroup.add(Nisha)

fishgroup.add(Nimit)

fishgroup.add(Stephanie)

fishgroup.add(Shannon)

fishgroup.add(Ben)

fishgroup.add(Paige)

fishgroup.add(Natalie)

fishgroup.add(Elise)

fishgroup.add(Nick)

 

def game():

    screen.fill((0,0,100))

    fishgroup.draw(screen)

    fishgroup.update()

    

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

 

main()