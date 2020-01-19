import pygame


def squares(x, y, w, h, color):

    pygame.draw.rect(gameDisplay, color, [x, y, w, h])


def drawBoard():

    black = (66, 134, 244)
    white = (143, 155, 175)
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    height = 100
    for _ in range(3):
        for _ in range(3):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, white)
            else:
                squares(xpos, ypos, width, height, black)
            xpos += 100
            color += 1
        ypos += 100
        xpos = 0


def player1(mx, my):
    global positionArray
    if 0 <= mx <= 100 and 0 <= my <= 100:
        gameDisplay.blit(x, (0, 0))
        positionArray[0][0] = 'x'
    elif 100 <= mx <= 200 and 0 <= my <= 100:
        gameDisplay.blit(x, (100, 0))
        positionArray[0][1] = 'x'
    elif 200 <= mx <= 300 and 0 <= my <= 100:
        gameDisplay.blit(x, (200, 0))
        positionArray[0][2] = 'x'
    elif 0 <= mx <= 100 and 100 <= my <= 200:
        gameDisplay.blit(x, (0, 100))
        positionArray[1][0] = 'x'
    elif 100 <= mx <= 200 and 100 <= my <= 200:
        gameDisplay.blit(x, (100, 100))
        positionArray[1][1] = 'x'
    elif 200 <= mx <= 300 and 100 <= my <= 200:
        gameDisplay.blit(x, (200, 100))
        positionArray[1][2] = 'x'
    elif 0 <= mx <= 100 and 200 <= my <= 300:
        gameDisplay.blit(x, (0, 200))
        positionArray[2][0] = 'x'
    elif 100 <= mx <= 200 and 200 <= my <= 300:
        gameDisplay.blit(x, (100, 200))
        positionArray[2][1] = 'x'
    elif 200 <= mx <= 300 and 200 <= my <= 300:
        gameDisplay.blit(x, (200, 200))
        positionArray[2][2] = 'x'


def player2(mx, my):
    global positionArray
    if 0 <= mx <= 100 and 0 <= my <= 100:
        gameDisplay.blit(o, (0, 0))
        positionArray[0][0] = 'o'
    elif 100 <= mx <= 200 and 0 <= my <= 100:
        gameDisplay.blit(o, (100, 0))
        positionArray[0][1] = 'o'
    elif 200 <= mx <= 300 and 0 <= my <= 100:
        gameDisplay.blit(o, (200, 0))
        positionArray[0][2] = 'o'
    elif 0 <= mx <= 100 and 100 <= my <= 200:
        gameDisplay.blit(o, (0, 100))
        positionArray[1][0] = 'o'
    elif 100 <= mx <= 200 and 100 <= my <= 200:
        gameDisplay.blit(o, (100, 100))
        positionArray[1][1] = 'o'
    elif 200 <= mx <= 300 and 100 <= my <= 200:
        gameDisplay.blit(o, (200, 100))
        positionArray[1][2] = 'o'
    elif 0 <= mx <= 100 and 200 <= my <= 300:
        gameDisplay.blit(o, (0, 200))
        positionArray[2][0] = 'o'
    elif 100 <= mx <= 200 and 200 <= my <= 300:
        gameDisplay.blit(o, (100, 200))
        positionArray[2][1] = 'o'
    elif 200 <= mx <= 300 and 200 <= my <= 300:
        gameDisplay.blit(o, (200, 200))
        positionArray[2][2] = 'o'


def occupied(mx, my):
    global positionArray
    occupiedFlag = False
    if 0 <= mx and mx <= 100 and 0 <= my <= 100:
        if positionArray[0][0] == 'x' or positionArray[0][0] == 'o':
            occupiedFlag = True
    elif 100 <= mx <= 200 and 0 <= my <= 100:
        if positionArray[0][1] == 'x' or positionArray[0][1] == 'o':
            occupiedFlag = True
    elif 200 <= mx <= 300 and 0 <= my <= 100:
        if positionArray[0][2] == 'x' or positionArray[0][2] == 'o':
            occupiedFlag = True
    elif 0 <= mx <= 100 and 100 <= my <= 200:
        if positionArray[1][0] == 'x' or positionArray[1][0] == 'o':
            occupiedFlag = True
    elif 100 <= mx <= 200 and 100 <= my <= 200:
        if positionArray[1][1] == 'x' or positionArray[1][1] == 'o':
            occupiedFlag = True
    elif 200 <= mx <= 300 and 100 <= my <= 200:
        if positionArray[1][2] == 'x' or positionArray[1][2] == 'o':
            occupiedFlag = True
    elif 0 <= mx <= 100 and 200 <= my <= 300:
        if positionArray[2][0] == 'x' or positionArray[2][0] == 'o':
            occupiedFlag = True
    elif 100 <= mx <= 200 and 200 <= my <= 300:
        if positionArray[2][1] == 'x' or positionArray[2][1] == 'o':
            occupiedFlag = True
    elif 200 <= mx <= 300 and 200 <= my <= 300:
        if positionArray[2][2] == 'x' or positionArray[2][2] == 'o':
            occupiedFlag = True
    return occupiedFlag


pygame.init()
gameDisplay = pygame.display.set_mode((300, 350))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
drawBoard()
x = pygame.transform.scale(pygame.image.load('x.png'), (100, 100))
o = pygame.transform.scale(pygame.image.load('o.png'), (100, 100))
quitGame = False
playerOrd = 0
positionArray = [[0 for col in range(3)]for row in range(3)]
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render("Player 1 wins", False, (255, 255, 255))
textsurface2 = myfont.render("Player 2 wins", False, (255, 255, 255))

while not quitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit = True
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            mx, my = pygame.mouse.get_pos()
            taken = occupied(mx, my)
            while taken:
                thisEvent = pygame.event.wait()
                if thisEvent.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    taken = occupied(mx, my)
                elif thisEvent.type == pygame.QUIT:
                    pygame.quit = True
                    quit()
            if playerOrd % 2 == 0:

                player1(mx, my)

            else:

                player2(mx, my)
            playerOrd += 1
        if positionArray[0][0] == 'x' and positionArray[0][1] == 'x' and positionArray[0][2] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 50), (300, 50), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[0][0] == 'o' and positionArray[0][1] == 'o' and positionArray[0][2] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 50), (300, 50), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()
        if positionArray[1][0] == 'x' and positionArray[1][1] == 'x' and positionArray[1][2] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 150), (300, 150), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[1][0] == 'o' and positionArray[1][1] == 'o' and positionArray[1][2] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 150), (300, 150), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()
        if positionArray[2][0] == 'x' and positionArray[2][1] == 'x' and positionArray[2][2] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 250), (300, 250), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[2][0] == 'o' and positionArray[2][1] == 'o' and positionArray[2][2] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 250), (300, 250), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()
        if positionArray[0][0] == 'x' and positionArray[1][0] == 'x' and positionArray[2][0] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (50, 0), (50, 300), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[0][0] == 'o' and positionArray[1][0] == 'o' and positionArray[2][0] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (50, 0), (50, 300), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()
        if positionArray[0][1] == 'x' and positionArray[1][1] == 'x' and positionArray[2][1] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (150, 0), (150, 300), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[0][1] == 'o' and positionArray[1][1] == 'o' and positionArray[2][1] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (150, 0), (150, 300), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()
        if positionArray[0][2] == 'x' and positionArray[1][2] == 'x' and positionArray[2][2] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (250, 0), (250, 300), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[0][2] == 'o' and positionArray[1][2] == 'o' and positionArray[2][2] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (250, 0), (250, 300), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()
        if positionArray[0][0] == 'x' and positionArray[1][1] == 'x' and positionArray[2][2] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 0), (300, 300), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[0][0] == 'o' and positionArray[1][1] == 'o' and positionArray[2][2] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (0, 0), (300, 300), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()
        if positionArray[0][2] == 'x' and positionArray[1][1] == 'x' and positionArray[2][0] == 'x':
            pygame.draw.line(gameDisplay, (0, 255, 0), (300, 0), (0, 300), 6)
            gameDisplay.blit(textsurface, (60, 305))
            pygame.display.update()
        if positionArray[0][2] == 'o' and positionArray[1][1] == 'o' and positionArray[2][0] == 'o':
            pygame.draw.line(gameDisplay, (0, 255, 0), (300, 0), (0, 300), 6)
            gameDisplay.blit(textsurface2, (60, 305))
            pygame.display.update()

        pygame.display.update()
        clock.tick(60)


















