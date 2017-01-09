"""
To do:
- continue breaking up code in this file
   = remove functions from here - getting back variables gave an error - solve?
   - find a way to not declare sentences twice

"""


import pygame

import library
import block_builder
import recipes

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



#def check_if_sense(block1
#####Declare variable:#####
sentenc_es = [
['bonne', 'chance'],
['bonne', 'annee']
]


def check(block):
    if block.active == True:
        if block.y >= 450:
            print 'hit bottom'
            #block.test = True
            landed_blocks.add(block)
            block.active = False
        elif pygame.sprite.spritecollideany(block, landed_blocks, False):
            print 'collided'
            collided = pygame.sprite.spritecollide(block, landed_blocks, False)
            for each_block in collided:
                check_aligned(block, each_block)
            landed_blocks.add(block)
            block.active = False


def check_aligned(block1,block2):
    if abs(block1.x - block2.x) < 25 or (block1.x + 100) == block2.x:
        print 'words', block1.word, block2.word
        for sentence in sentenc_es:
            if sentence[0] == block1.word and sentence[1] == block2.word:
                block1.color = RED
                block2.color = RED


done = False #Runs until closed
clock = pygame.time.Clock() ##Manage speed
game_over = False

blocks = []
all_blocks = pygame.sprite.Group()
landed_blocks = pygame.sprite.Group()

change_y = 1
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
                change_y = 4
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_x = 0
            elif event.key == pygame.K_DOWN:
                change_y = 2

    ###### Game logic goes here: ######

    #Add new block when there are no active blocks
    if len(blocks) <1 or blocks[len(blocks)-1].active == False:
        word = library.get_word()
        block = block_builder.Block(word, BLUE, BLACK)
        blocks.append(block)
        print 'blocks', blocks
        for block in blocks:
            print block.active
        print '\n'
        print blocks[len(blocks)-1].active
        print '\n'
        print 'landed blocks', landed_blocks


    ##### Drawing logic goes here: #####
    screen.fill(WHITE) #clear screen before Drawing

    for block in blocks:

        check(block) # check all

        if block.active == True:
            block.move(change_x, change_y)
        elif block.color == RED: #red means its been used to form a sentence
            block.move(0, 3)

        block.draw(screen) # draw all

    pygame.display.flip() #update view

    clock.tick(60) #limit to 60 frames per second


pygame.quit() #End game properly
