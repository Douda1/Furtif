import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1920,1017),
                                 pygame.RESIZABLE)

clock = pygame.time.Clock()

icone = pygame.image.load('Graphique/logo.png')

pygame.display.set_icon(icone)

pygame.display.set_caption("Histoire.odt — LibreOffice Writer")



AvionX = 200
AvionY = 200
ImageAvion = pygame.image.load('Graphique/logo.png')
MissileX = AvionX
MissileY = AvionY
MissileRect = pygame.Rect(MissileX,MissileY,5,10)


Activé = False










while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    Background = pygame.image.load('Graphique/Background.png')
    # Do logical updates here.
    # -----------------------------------------------------------------------------------------------------------------------
    screen.blit(Background,(0,0))
    
    AvionRect = pygame.Rect(AvionX,AvionY,10,10)
    MissileRect = pygame.Rect(MissileX,MissileY,5,10)
    
    
    if event.type == pygame.KEYDOWN:
        time.sleep(0.5)
        if event.key == pygame.K_LCTRL:
            if Activé:
                Activé = False
            else:
                Activé = True
    
    if pygame.key.get_pressed()[pygame.K_d]:
        AvionX += 10
    if pygame.key.get_pressed()[pygame.K_q]:
        AvionX -= 10
    if pygame.key.get_pressed()[pygame.K_s]:
        AvionY += 10
    if pygame.key.get_pressed()[pygame.K_z]:
        AvionY -= 10

    
    
    if Activé:
        MissileY -= 10
        if MissileY ==  100:
            MissileY = AvionY
            MissileX = AvionX
        pygame.draw.rect(screen,(255,0,255), AvionRect)
        pygame.draw.rect(screen,(0,255,0), MissileRect)
        

    print(AvionX)
    
    
    
    
    
    

    
    
    # -----------------------------------------------------------------------------------------------------------------------

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)