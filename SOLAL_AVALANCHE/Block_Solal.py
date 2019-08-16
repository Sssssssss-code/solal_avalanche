import pygame
class Block():
    def __init__(self,colour,gridXpos,gridYpos):
        self.colour=colour#the colour
        self.gridXpos = int(gridXpos) # sets x position
        self.gridYpos=int(gridYpos)#sets y position
        self.size=25#sets the size
    def draw(self,screen):#draws the rectangle
        pygame.draw.rect(screen, self.colour, [self.gridXpos*self.size, self.gridYpos*self.size, self.size-1, self.size-1], 0)