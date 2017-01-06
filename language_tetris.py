sentences = [
['bonne', 'chance'],
['bonne', 'annee']
]

import pygame
import random

pygame.init()

#Define colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#Open window for game
size = (700, 500)
screen = pygame.display.set_mode(size)

#Set title
pygame.display.set_caption("Language-Tetris")


#####Declare functions and objects#####

class Block(pygame.sprite.Sprite):
    def __init__(self, word):
        pygame.sprite.Sprite.__init__(self)
        #self.id = this_id
        self.x = 275
        self.y = 0
        self.word = word
        self.change_x = 0
        self.change_y = 0
        self.color = BLUE
        self.active = True
        self.image = pygame.Surface((100,50))
        self.rect = self.image.get_rect()
        #self.landed = False
    def move(self):
        if self.active == True:
            #self.x += self.change_x
            self.y += change_y
            self.rect.move_ip(0,change_y)
            if self.x >= 600 and change_x > 0:
                self.x = 600
            elif self.x <= 0 and change_x < 0:
                self.x = 0
            else:
                self.x = self.x + change_x
                self.rect.move_ip(change_x,0)
        else:
            self.x = self.x
            self.y = self.y
    def draw(self, screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,100,50],0)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(self.word,True,BLACK)
        screen.blit(text, [self.x+15, self.y+15])
    def check(self):
        if self.active == True:
            if self.y >= 450:
                self.active = False
                #self.landed = True
                landed_blocks.add(self)
            elif pygame.sprite.spritecollideany(self, landed_blocks, False):
                collided = pygame.sprite.spritecollide(self, landed_blocks, False)
                for block in collided:
                    check_aligned(self, block)
                print 'collision'
                self.active = False
                #self.landed = True
                landed_blocks.add(self)

def get_word():
    sentence = sentences[random.randint(0,(len(sentences)-1))]
    word = sentence[random.randint(0,(len(sentence)-1))]
    return word

def check_aligned(block1,block2):
    if abs(block1.x - block2.x) < 25:
        print 'words', block1.word, block2.word
        for sentence in sentences:
            if sentence[0] == block1.word and sentence[1] == block2.word:
                block1.color = RED
                block2.color = RED
                block1.y = 500
                block2.y = 500

#def check_if_sense(block1
#####Declare variable:#####
done = False #Runs until closed
clock = pygame.time.Clock() ##Manage speed
game_over = False

blocks = []
all_blocks = pygame.sprite.Group()
landed_blocks = pygame.sprite.Group()

change_y = 0
change_x = 0
###### MAIN LOOP #####
while not done:

    ###Add game over loop here

    #####Main event loop: (ALL USER EVENTS SHOULD GO HERE)
    for event in pygame.event.get(): #user does something
        if event.type == pygame.QUIT: #if user closes:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -2
            if event.key == pygame.K_RIGHT:
                change_x = 2
            if event.key == pygame.K_DOWN:
                change_y = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_x = 0
            elif event.key == pygame.K_DOWN:
                change_y = 0

    ###### Game logic goes here: ######

    #Add new block:
    if len(blocks) <1 or blocks[len(blocks)-1].active == False:
        word = get_word()
        block = Block(word)
        blocks.append(block)
        print 'blocks', blocks
        for block in blocks:
            print block.active
        print '\n'
        print blocks[len(blocks)-1].active
        print '\n'
        print 'landed blocks', landed_blocks



    #Check if game over
    #game_over = check_if_game_over()


    ##### Drawing logic goes here: #####
    screen.fill(WHITE) #clear screen before Drawing

    for each_block in blocks:
    #    if each_block.active == True and each_block.landed == False:
        each_block.check()
        each_block.move()
        each_block.draw(screen)

    pygame.display.flip() #update view

    clock.tick(60) #limit to 60 frames per second


pygame.quit() #End game properly
