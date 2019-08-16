
import random
import pygame
from Block_Solal import Block
from Gameboard_Solal import gameboardwidth,gameboardheight,activeBoardColour,activeBoardSpot
# Define some colours RGB
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
MAGENTA = (255,0,255)
TURQUOISE = (0,206,209)
# All of the colours
ALLCOLOURS = [WHITE,GREEN,RED,BLUE,YELLOW,MAGENTA,TURQUOISE,BLACK]
# each array element is 1 block's coordinates
ZSHAPE=[[(gameboardwidth/2)-1,0],[(gameboardwidth/2)-2,0],[(gameboardwidth/2)-1,1],[gameboardwidth/2,1]]
# S SHAPE
SSHAPE = [[(gameboardwidth/2)-1,0],[gameboardwidth/2,0],[(gameboardwidth/2)-2,1],[(gameboardwidth/2)-1,1]]
# LINE
LINESHAPE = [[(gameboardwidth/2)-1,0],[(gameboardwidth/2)-2,0],[(gameboardwidth/2),0],[(gameboardwidth/2)+1,0]]
# SQUARE
SQUARESHAPE = [[(gameboardwidth/2)-1,0], [gameboardwidth/2,0], [gameboardwidth/2,1],[(gameboardwidth/2)-1,1]]
# L
LSHAPE = [[(gameboardwidth/2)-1,1], [(gameboardwidth/2)-1,0],[(gameboardwidth/2)-1,2],[gameboardwidth/2,2]]
# Mirror L
MLSHAPE = [[(gameboardwidth/2),1], [(gameboardwidth/2),0],[(gameboardwidth/2),2],[(gameboardwidth/2)-1,2]]
#T Shape
TSHAPE = [[(gameboardwidth/2)-1,1],[(gameboardwidth/2)-1,0],[(gameboardwidth/2),1],[(gameboardwidth/2)-2,1]]
# All Shapes
ALLSHAPES = [ZSHAPE, SSHAPE, LINESHAPE, SQUARESHAPE, LSHAPE, MLSHAPE, TSHAPE]


class Shape():  #creates and moves the shapes
    def __init__(self):
        self.numblocks=4
        randomNum=random.randrange(7)
        self.shape=ALLSHAPES[randomNum]
        self.colour=ALLCOLOURS[randomNum]
        self.blockList= []
        self.active=True
        self.pause=False
        for i in range(self.numblocks):
            self.blockList.append(Block(self.colour,self.shape[i][0],self.shape[i][1]))
    def draw(self,screen):#draws the shapes
        for i in range(self.numblocks):
            self.blockList[i].draw(screen)
    def moveLeft(self):#moves all blocks to the left
        if not self.pause:
            blocked = False
            for i in range(4):
                if self.blockList[i].gridXpos == 0 or activeBoardSpot[self.blockList[i].gridXpos-1][self.blockList[i].gridYpos]:
                    blocked = True
            if blocked == False:
                for i in range(self.numblocks):
                    self.blockList[i].gridXpos-=1
    def moveRight(self):#moves all blocks to the right
        if not self.pause:
            blocked = False
            for i in range(4):
                if self.blockList[i].gridXpos == gameboardwidth - 1 or activeBoardSpot[self.blockList[i].gridXpos+1][self.blockList[i].gridYpos]:
                    blocked = True
            if blocked == False:
                for i in range(self.numblocks):
                    self.blockList[i].gridXpos+=1
    def moveDown(self):
        if not self.pause:
            blocked= False
            for i in  range(4):
                if self.blockList[i].gridYpos == gameboardheight-1 or activeBoardSpot[self.blockList[i].gridXpos][self.blockList[i].gridYpos+1]:
                    blocked=True
            if blocked==False:
                for i in range(4):
                    self.blockList[i].gridYpos +=1
    def rotateCW(self):
        if not self.pause:
            if self.shape!= SQUARESHAPE:
                newBlockX=[0,0,0,0]
                newBlockY=[0,0,0,0]
                canrotate=True
                for i in range(self.numblocks):
                    newBlockX[i]= -(self.blockList[i].gridYpos - self.blockList[0].gridYpos)+self.blockList[0].gridXpos
                    newBlockY[i]= (self.blockList[i].gridXpos - self.blockList[0].gridXpos)+self.blockList[0].gridYpos
                    if newBlockX[i]<0 or newBlockX[i]>= gameboardwidth-1:#checks if rotation is possible
                        canrotate=False
                    elif newBlockY[i]<0 or newBlockY[i] >= gameboardheight-1:
                        canrotate=False
                    elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                        canrotate=False
                if canrotate:
                    for i in  range(self.numblocks):
                        self.blockList[i].gridXpos=newBlockX[i]
                        self.blockList[i].gridYpos=newBlockY[i]
    def rotateCCW(self):
        if not self.pause:
                if self.shape!= SQUARESHAPE:
                    newBlockX=[0,0,0,0]
                    newBlockY=[0,0,0,0]
                    canrotate=True
                    for i in range(self.numblocks):
                        newBlockX[i]= (self.blockList[i].gridYpos - self.blockList[0].gridYpos)+self.blockList[0].gridXpos
                        newBlockY[i]= -(self.blockList[i].gridXpos - self.blockList[0].gridXpos)+self.blockList[0].gridYpos
                        if newBlockX[i]<0 or newBlockX[i]>= gameboardwidth-1:#checks if rotation is possible
                            canrotate=False
                        elif newBlockY[i]<0 or newBlockY[i] >= gameboardheight-1:
                            canrotate=False
                        elif activeBoardSpot[newBlockX[i]][newBlockY[i]]:
                            canrotate=False
                    if canrotate:
                        for i in  range(self.numblocks):
                            self.blockList[i].gridXpos=newBlockX[i]
                            self.blockList[i].gridYpos=newBlockY[i]
    def falling(self):
        if not self.pause:
            for i in range(4):
                if self.blockList[i].gridYpos==gameboardheight-1 or activeBoardSpot[self.blockList[i].gridXpos][self.blockList[i].gridYpos+1]:
                    self.hitBottom()
            for i in range(4):
                if self.active:
                    self.blockList[i].gridYpos +=1


    def hitBottom(self):
        for i in range(4):
            activeBoardSpot[self.blockList[i].gridXpos][self.blockList[i].gridYpos]=True
            activeBoardColour[self.blockList[i].gridXpos][self.blockList[i].gridYpos]= self.blockList[i].colour
        self.active=False

    def drop(self):
        if not self.pause:
            while self.active:
                for i in range(4):
                    if self.blockList[i].gridYpos==gameboardheight-1 or activeBoardSpot[self.blockList[i].gridXpos][self.blockList[i].gridYpos+1]:
                        self.hitBottom()
                for i in range(4):
                    if self.active:
                        self.blockList[i].gridYpos+=1
    def drawNextShape(self,screen):
        for i in range(self.numblocks):
            pygame.draw.rect(screen,self.blockList[i].colour,[self.blockList[i].gridXpos*self.blockList[i].size+325,self.blockList[i].gridYpos*self.blockList[i].size+150,self.blockList[i].size-1,self.blockList[i].size-1],0)