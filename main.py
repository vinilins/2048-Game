import pygame
from pygame.locals import *
import random

pygame.init()

time = pygame.time.Clock()
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (149,149,149)
RED = (255,0,0)

WIDTH_SCREEN = 450
HEIGHT_SCREEN = 600

CONST = 80

screen = pygame.display.set_mode((WIDTH_SCREEN,HEIGHT_SCREEN))

FONT = pygame.font.Font('leadcoat.ttf', 72)
FONT35 = pygame.font.Font('leadcoat.ttf', 35)
FONT3 = pygame.font.Font('leadcoat.ttf', 35)
TEXT_TITLE = FONT.render('2048 ', True, WHITE)
TEXT_TITLE_POS = TEXT_TITLE.get_rect()
TEXT_TITLE_POS.center = (WIDTH_SCREEN/4, 75)
TEXT_GAMELOSE = FONT3.render('GAME OVER ', True, WHITE)
TEXT_GAMELOSE_POS = TEXT_GAMELOSE.get_rect()
TEXT_GAMELOSE_POS.center = (WIDTH_SCREEN/2, 205)

class Block():

    def __init__(self, position):
        listNumber = [2,4]
        self.value = listNumber[random.randint(0,1)] 
        self.position = position
        if self.position in [0,1,2,3,4]:
            self.top = 155
            self.left = 30+(self.position*80)
        elif self.position in [5,6,7,8,9]:
            self.top = 155+(1*80)
            self.left = 30+((self.position%5)*80)
        elif self.position in [10,11,12,13,14]:
            self.top = 155+(2*80)
            self.left = 30+((self.position%5)*80)
        elif self.position in [15,16,17,18,19]:
            self.top = 155+(3*80)
            self.left = 30+((self.position%5)*80)
        elif self.position in [20,21,22,23,24]:
            self.top = 155+(4*80)
            self.left = 30+((self.position%5)*80)
        self.color = GRAY
        self.size = (self.left,self.top,75,75)
        self.text = FONT35.render(f'{self.value}', True, WHITE)
        self.text_position = self.text.get_rect() 
        self.text_position.center = (self.left+35,self.top+35)
    
    def update(self):
        if self.position in [0,1,2,3,4]:
            self.top = 155
            self.left = 30+(self.position*80)
        elif self.position in [5,6,7,8,9]:
            self.top = 155+(1*80)
            self.left = 30+((self.position%5)*80)
        elif self.position in [10,11,12,13,14]:
            self.top = 155+(2*80)
            self.left = 30+((self.position%5)*80)
        elif self.position in [15,16,17,18,19]:
            self.top = 155+(3*80)
            self.left = 30+((self.position%5)*80)
        elif self.position in [20,21,22,23,24]:
            self.top = 155+(4*80)
            self.left = 30+((self.position%5)*80)
        self.size = (self.left,self.top,75,75)
        self.text = FONT35.render(f'{self.value}', True, WHITE)
        self.text_position = self.text.get_rect() 
        self.text_position.center = (self.left+35,self.top+35)
    
def selectionSort(array):
    for i in range(len(array)): 
        min_idx = i 
        for j in range(i+1, len(array)): 
            if array[min_idx].position > array[j].position: 
                min_idx = j 
        array[i], array[min_idx] = array[min_idx], array[i]
    for e in array:
        print(e.position)
    return array

def BlocksEquals(blocks,block1,block2):
    if block1.value == block2.value:
        pass
    return blocks

def upBlocks(blocks):
    blocks = selectionSort(blocks)
    count = 0
    for i in range(len(blocks)):
        haveBlockUp = False
        while True:
            for e in blocks:
                if e.position == blocks[i].position - 5 or blocks[i].position - 5 <0:
                    haveBlockUp = True
                    eEqual = e
                    break
            if haveBlockUp:
                blocks = BlocksEquals(blocks,blocks[i],eEqual)
                break
            count+=1
            blocks[i].position -= 5
            blocks[i].update()
    return count

def downBlocks(blocks):
    blocks = selectionSort(blocks)
    count = 0
    for i in range(len(blocks)-1,-1,-1):
        haveBlockDown = False
        while True:
            for e in blocks:
                if e.position == blocks[i].position + 5 or blocks[i].position + 5 >24:
                    haveBlockDown = True
                    eEqual = e
                    break
            if haveBlockDown:
                blocks = BlocksEquals(blocks,blocks[i],eEqual)
                break
            count+=1
            blocks[i].position +=5
            blocks[i].update()
    return count

def leftBlocks(blocks):
    blocks = selectionSort(blocks)
    count = 0
    for i in range(len(blocks)):
        haveBlockLeft = False
        while True:
            for e in blocks:
                if e.position == blocks[i].position - 1 or blocks[i].position%5 - 1 <0:
                    haveBlockLeft = True
                    eEqual = e
            if haveBlockLeft:
                blocks = BlocksEquals(blocks,blocks[i],eEqual)
                break
            count+=1
            blocks[i].position -=1
            blocks[i].update()
    return count

def rightBlocks(blocks):
    blocks = selectionSort(blocks)
    count = 0
    for i in range(len(blocks)-1,-1,-1):
        haveBlockRight = False
        while True:
            for e in blocks:
                if e.position == blocks[i].position + 1 or blocks[i].position%5 + 1 > 4:
                    haveBlockRight = True
                    eEqual = e
            if haveBlockRight:
                blocks = BlocksEquals(blocks,blocks[i],eEqual)
                break
            count+=1
            blocks[i].position +=1
            blocks[i].update()
    return count



blockGroup = []
block = Block(0)
blockGroup.append(block)

control = False

while True:

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, (27,152,401,401))
    pygame.draw.line(screen, BLACK, (25,232),(430,232), 1)
    pygame.draw.line(screen, BLACK, (25,232+CONST),(430,232+CONST), 1)
    pygame.draw.line(screen, BLACK, (25,232+CONST*2),(430,232+CONST*2), 1)
    pygame.draw.line(screen, BLACK, (25,232+CONST*3),(430,232+CONST*3), 1)

    pygame.draw.line(screen, BLACK, (107,150),(107,555), 1)
    pygame.draw.line(screen, BLACK, (107+CONST,150),(107+CONST,555), 1)
    pygame.draw.line(screen, BLACK, (107+CONST*2,150),(107+CONST*2,555), 1)
    pygame.draw.line(screen, BLACK, (107+CONST*3,150),(107+CONST*3,555), 1)

    verify = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                verify = upBlocks(blockGroup)
            if event.key == pygame.K_DOWN:
                verify = downBlocks(blockGroup)
            if event.key == pygame.K_LEFT:
                verify = leftBlocks(blockGroup)
            if event.key == pygame.K_RIGHT:
                verify = rightBlocks(blockGroup)

            
            listNum = []
            for i in range(25):
                listNum.append(i)
            listPositions = []
            for e in blockGroup:
                if e.position in listNum:
                    listNum.remove(e.position)
            if listNum == []:
                pygame.quit()
                quit()
            elif verify!=0:
                block = Block(random.choice(listNum))
                blockGroup.append(block)

    screen.blit(TEXT_TITLE,TEXT_TITLE_POS)
    for e in blockGroup:
        pygame.draw.rect(screen,e.color,e.size)
        screen.blit(e.text,e.text_position)
    
    time.tick(FPS)
    pygame.display.update()
