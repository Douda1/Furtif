
import pygame
import time
import random

pygame.init()


screen = pygame.display.set_mode((1920, 1017),
                                 pygame.RESIZABLE)

x, y = screen.get_size()
clock = pygame.time.Clock()

icone = pygame.image.load('Graphique\logo.png')

pygame.display.set_icon(icone)

pygame.display.set_caption("Histoire.odt — LibreOffice Writer")

myfont = pygame.font.SysFont("monospace", 15)
avionim = pygame.image.load('Graphique\Avion.png')
Score = 0
AvionX = 200
AvionY = 200
ImageAvion = pygame.image.load('Graphique/logo.png')
imageene = pygame.image.load('Graphique/lenemy.png')
MissileX = AvionX
MissileY = AvionY
MissileRect = pygame.Rect(MissileX,MissileY,5,10)
enemyx = 200
enemyy = 200
enemyRect = pygame.Rect(enemyx,enemyy,70,100)

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
    x, y = screen.get_size()
    reBackground = pygame.transform.scale(Background, (x, y))
    reAvion = pygame.transform.scale(avionim, (120, 100))
    reenemy = pygame.transform.scale(imageene, (70, 100))
    screen.blit(reBackground,(0,0))
    print(x,y)
    AvionRect = pygame.Rect(AvionX,AvionY,0,0)
    MissileRect = pygame.Rect(MissileX,MissileY,10,10)
    enemyRect = pygame.Rect(enemyx,enemyy,70,100)
    
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
        MissileY -= 20
        if MissileY <  100:
            MissileY = AvionY
            MissileX = AvionX+55
        pygame.draw.rect(screen,(255,0,255),AvionRect)
        pygame.draw.rect(screen,(0,255,0), MissileRect)
        pygame.draw.rect(screen,(32,32,32), enemyRect)
        
    if Activé:
        screen.blit(reenemy,(enemyx,enemyy))
        screen.blit(reAvion,(AvionX,AvionY))
    
    if Activé:
        enemyy += 11
        if enemyy > 1000:
            enemyy = 100
            Score = 0
    if pygame.Rect.colliderect(enemyRect,MissileRect):
        Score += 1
        enemyy = 100
        enemyx = random.randint(100, 500)
    if Activé:
        theScore = myfont.render(str(Score) , 1, (255,255,255))
        LeScore = myfont.render("Score : " , 1, (255,255,255))
        screen.blit(theScore, (125, 150))
        screen.blit(LeScore, (40, 150))




    
    
    
    
    
    

    
    
    # -----------------------------------------------------------------------------------------------------------------------

    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)