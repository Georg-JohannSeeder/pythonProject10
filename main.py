import pygame, sys

pygame.init()

# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)

#graafika laadimine
ralli = pygame.image.load("bg_rally.jpg")
pauto = pygame.image.load("f1_red.png")
sauto = pygame.image.load("f1_blue.png")

#kiirus ja asukoht
posX, posY = 420, 15
speedY = 0.5

gameover = False
while not gameover:
    #mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()

    #pildi lisamine ekraanile
    screen.blit(ralli, (0,0))
    screen.blit(pauto, (posX, posY))
    screen.blit(sauto, (posX, posY))

    posY += speedY

    #graafika kuvamine ekraanil
    pygame.display.flip()


pygame.quit()
