import pygame,random,sys,time
pygame.init()  #pygame moodul
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Animeerimine")

clock = pygame.time.Clock()

startTime = time.time()  #aeg alguses
score = 0

#taust
bg = pygame.image.load("bg_rally.jpg")
bgposX = 0
bgspeedX = -3

#auto pildid
f1Blue = pygame.image.load("f1_blue.png")
f1Blue2 = pygame.image.load("f1_blue.png")
f1Red = pygame.image.load("f1_red.png")

gameover = False

blueSpeedY = 3

bluePosY = random.randint(0, 100)
blue2PosY = random.randint(0, 100)
redPosX, redPosY = 298, 390
redSpeedY = 0
bluePosX = random.randint(300, 460)
blue2PosX = random.randint(130, 280)

while not gameover:
    clock.tick(120)  #kaadrisagedus

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #lisatakse taustapildid
    screen.blit(bg, (0, bgposX))

    #kiirused
    bgposX -= bgspeedX

    #taustapildi loop
    if bgposX >= 480:
        bgposX = -480

    #lisatakse sinised autod
    screen.blit(f1Blue, (bluePosX, bluePosY))
    screen.blit(f1Blue2, (blue2PosX, blue2PosY))

    #liigutatakse autosi
    bluePosY += blueSpeedY + 0.8
    blue2PosY += blueSpeedY + 1

    #lisatakse punane auto
    screen.blit(f1Red, (redPosX, redPosY))
    redPosY += redSpeedY

    #kuvatakse skoor
    screen.blit(pygame.font.Font(None, 30).render(f"Skoor: {score}", True, [255, 255, 255]), [0, 0])

    #autode positsiooni taastamine
    if bluePosY >= 480:
        bluePosY = -120
        score += 1
        bluePosX = random.randint(130, 280)
    if blue2PosY >= 480:
        blue2PosY = -120
        score += 1  #
        blue2PosX = random.randint(300, 480)

    if redPosY >= 480:  #punane auto pole ekraanil näha
        redPosY = -120  #taastame ta positsiooni

    #kui autod saavad kokku
    if redPosY + 55 >= bluePosY >= redPosY - 55:
        if redPosX + 50 >= bluePosX >= redPosX - 50:
            gameover = True

    if redPosY + 55 >= bluePosY >= redPosY - 55:
        if redPosX + 50 >= bluePosX >= redPosX - 50:
            gameover = True

    #suurendakse kiirust iga minuti tagant
    if time.time() % 60 == 0:
        blueSpeedY += 0.5  #suurendakse kiirust 1 võtta

    #kuvame aega
    screen.blit(pygame.font.Font(None, 20).render(f"Aeg: {int(time.time() - startTime)}",
                                                  True, [255, 255, 255]), [0, 20])
    pygame.display.flip()

while True:
    if gameover:
        screen.blit(pygame.font.Font(None, 50).render("Mäng läbi", True, [255, 255, 255]), [230, 300])
        screen.blit(pygame.font.Font(None, 50).render(f"Skoor: {score}", True, [255, 255, 255]),
                    [240, 200])
        pygame.display.flip()  # uuendatakse ekraani

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
