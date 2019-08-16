#importing everything needed from other files or libraries
import pygame
import time
from Shape_Solal import Shape
from Gameboard_Solal import Gameboard,gameboardheight
#defining colours
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
MAGENTA=(255,0,255)
TURQUOISE=(0,206,209)
GRIS=(142, 162, 198)


#checks if it is the min file
if __name__=="__main__":
    pygame.init()
    pygame.mixer.init()

#initialising everything
    size=(900,600)

    screen=pygame.display.set_mode(size)

    pygame.display.set_caption('Avalanche by Solal')
    myfont=pygame.font.Font('freesansbold.ttf',30)
    HSfont=pygame.font.Font('freesansbold.ttf',20)
    shape=Shape()#1st shape
    nextshape=Shape()
    gameboard=Gameboard(WHITE,shape.blockList[0].size)#our gameboard
    name=""
    delay=0
    pause=False
    slowtimedelay=0
    pygame.mixer.music.load('AvalancheBGM.mp3')
    pygame.mixer.music.play(-1)
    namelist=[0 for y in range(5)]
    scorelist=[0 for y in range(5)]
    HSfile= open("HighScores.txt","r")
    for i in  range(5):
        namelist[i]=HSfile.readline().rstrip('\n')
    for i in range(5):
        scorelist[i] = HSfile.readline().rstrip('\n')
    HSfile.close()

    done=False
    started=False

def keyCheck():
    if event.key==pygame.K_LEFT:
        shape.moveLeft()
    elif event.key==pygame.K_RIGHT:
        shape.moveRight()
    elif event.key==pygame.K_d:
        shape.moveDown()
    elif event.key == pygame.K_UP:
        shape.rotateCW()
    elif event.key == pygame.K_DOWN:
        shape.rotateCCW()
    elif event.key==pygame.K_SPACE and not shape.pause:
        gameboard.score+=(gameboardheight - shape.blockList[0].gridYpos )
        shape.drop()
    elif event.key==pygame.K_t and gameboard.numlowtime>0 and not shape.pause:
        gameboard.numlowtime-=1
        gameboard.slowtimeon=True
    elif event.key==pygame.K_s and gameboard.numswap>0 and not shape.pause:
        gameboard.numswap-=1
        gameboard.swapshape=True
    elif event.key==pygame.K_e and gameboard.numeraser>0 and not shape.pause:
        gameboard.numeraser-=1
        gameboard.clearButtomRow()
    elif event.key==pygame.K_q and not shape.pause:
        gameboard.score=999999
    elif event.key==pygame.K_p:
        shape.pause=not shape.pause




def drawScreen():
    screen.fill(BLACK)
    shape.draw(screen)
    nextshape.drawNextShape(screen)
    gameboard.drawGrid(screen)
    gameboard.draw(screen)
    scoretext = myfont.render("Score:" + str(gameboard.score), 1, WHITE)
    screen.blit(scoretext, (400, 400))
    linetext = myfont.render("Lines:" + str(gameboard.numlines), 1, WHITE)
    screen.blit(linetext, (400, 350))
    leveltext=myfont.render("Level:"+str(gameboard.level),1,WHITE)
    screen.blit(leveltext,(400,300))
    poweruptext=myfont.render("Power Ups:",1,WHITE)
    screen.blit(poweruptext,(50,525))
    numlowtimetext=myfont.render("x"+str(gameboard.numlowtime),1,WHITE)
    screen.blit(numlowtimetext,(310,525))
    slowtime_image=pygame.image.load("clock.png")
    screen.blit(slowtime_image,(250,515))
    numswaptext=myfont.render("x"+str(gameboard.numswap),1,WHITE)
    screen.blit(numswaptext,(435,525))
    swap_image=pygame.image.load("swap.png")
    screen.blit(swap_image,(375,515))
    numeraser = myfont.render("x" + str(gameboard.numeraser), 1, WHITE)
    screen.blit(numeraser,(570,525))
    eraser_image = pygame.image.load("eraser.png")
    screen.blit(eraser_image, (500, 515))
    nextshapetext = myfont.render("Next:" , 1, WHITE)
    screen.blit(nextshapetext, (400, 50))
    pygame.draw.rect(screen,WHITE,[400,100,6*shape.blockList[0].size,6*shape.blockList[0].size],1)
    highscoretext=myfont.render("High Scores:",1,WHITE)
    screen.blit(highscoretext,(575,50))
    pygame.draw.rect(screen,WHITE,[575,100,200,400],1)
    playernametext=myfont.render("Player:"+name,1,WHITE)
    screen.blit(playernametext,(665,525))
    for i in range(5):
        hsnametext=HSfont.render(str(namelist[i]),1,WHITE)
        hsscoretext=HSfont.render(str(scorelist[i]),1,WHITE)
        screen.blit(hsnametext,(580,i*25+125))
        screen.blit(hsscoretext,(700,i*25+125))
    if shape.pause:
        pygame.draw.rect(screen,WHITE,[420,270,20,60],0)
        pygame.draw.rect(screen,WHITE,[460,270,20,60],0)

    pygame.display.flip()

def checkHighScore  ():
    newhighscore = False
    tempnamelist = [0 for y in range(5)]
    tempscorelist = [0 for y in range(5)]
    for i in range(5):
        if gameboard.score > int(scorelist[i]) and newhighscore == False:
            newhighscore = True
            tempscorelist[i] = gameboard.score
            tempnamelist[i] = name
        elif newhighscore == True:
            tempscorelist[i] = scorelist[i-1]
            tempnamelist[i] = namelist[i-1]
        else:
            tempscorelist[i] = scorelist[i]
            tempnamelist[i] = namelist[i]

    for i in range(5):
        scorelist[i] = tempscorelist[i]
        namelist[i]  = tempnamelist[i]

    HSfile = open("HighScores.txt", "w")
    for i in range(5):
        HSfile.write(namelist[i] + '\n')

    for i in range(5):
        HSfile.write(str(scorelist[i]) + '\n')
    HSfile.close()


while not  started:
    titlescreen=pygame.image.load("Backdrop - Copy.png")
    enterednametext=myfont.render("Please Type Your Name In:",1,WHITE)
    nametext=myfont.render(name,1,WHITE)
    screen.blit(enterednametext,(200,200))
    screen.blit(nametext,(300,250))
    pygame.display.flip()
    screen.blit(titlescreen,(0,0))

    for event in  pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
            started=True
        if event.type==pygame.KEYDOWN:
            if event.key>=33 and event.key<=126 and len(name)<10:
                name=name+chr(event.key)
            if event.key ==pygame.K_BACKSPACE:
                name=name[:-1]
            if event.key==pygame.K_RETURN:
                if name =="":
                    name="Player 1"
                started=True

while not done:#checks if we want to quit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.KEYDOWN:#if a key is pressed
            keyCheck()
    delay+=1
    if delay>=10:
        shape.falling()
        delay=0
    if gameboard.slowtimeon:
        slowtimedelay+=1
        if slowtimedelay>50:
            slowtimedelay=0
            gameboard.slowtimeon=False
    if gameboard.swapshape:
        shape=nextshape
        nextshape=Shape()
        gameboard.swapshape=False
    if shape.active==False:
        gameboard.clearFullRows()
        shape=nextshape
        nextshape=Shape()
    if gameboard.checkLoss():
        checkHighScore()
        gameboard=Gameboard(WHITE,shape.blockList[0].size)
        slowtimedelay=0
        shape=Shape()
        nextshape=Shape()




    drawScreen()
    if (0.11-gameboard.level*0.01>=0):
        time.sleep(0.11 - gameboard.level * 0.01+gameboard.slowtimeon*0.1)
