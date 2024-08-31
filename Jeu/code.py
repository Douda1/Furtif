import pygame

pygame.init()

screen = pygame.display.set_mode((1920,1017),
                                 pygame.RESIZABLE)

clock = pygame.time.Clock()

icone = pygame.image.load('Graphique/logo.png')

pygame.display.set_icon(icone)

pygame.display.set_caption("Histoire.odt — LibreOffice Writer")

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    Background = pygame.image.load('Graphique/Background.png')
    # Do logical updates here.
    # ...
    print(screen)

    screen.fill("purple")  # Fill the display with a solid color
    screen.blit(Background,(0,0))
    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)