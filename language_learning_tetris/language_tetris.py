import pygame
import word_logic
import block_builder
import block_tracker
import game_functions

pygame.init()


#Open window for game
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Language-Tetris")

#####Declare game variable:#####
game_over = False #Runs until closed
clock = pygame.time.Clock() ##Manage speed

tracker = block_tracker.Tracker()

#Define colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

change_y = 1
change_x = 0
###### MAIN LOOP #####
while not game_over:

    ###Add game over loop here

    #####Main event loop: (ALL USER EVENTS SHOULD GO HERE)
    for event in pygame.event.get(): #user does something
        if event.type == pygame.QUIT: #if user closes:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -1
            if event.key == pygame.K_RIGHT:
                change_x = 1
            if event.key == pygame.K_DOWN:
                change_y = 2
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change_x = 0
            elif event.key == pygame.K_DOWN:
                change_y = 1

    ###### Game logic goes here: ######

    #~~Add new block when there are no active blocks
    if len(tracker.blocks) <1 or tracker.blocks[len(tracker.blocks)-1].active == False:
        word, units = word_logic.get_word()
        block = block_builder.Block(word,units)
        tracker.blocks.append(block)
        for block in tracker.blocks:
            print block.active



    #~~Draw new screen:
    screen.fill(WHITE)
    #~~Iterate through the blocks:
    for block in tracker.blocks:

        #tracker.check takes a block, and compares it against self.landed_blocks
        #it returns block, block it collided with (none if none)
        #***Later this needs to handle more than one collisions
        block, collided_with = tracker.check(block)

        if collided_with:

            #for each_block in collided_with:
                #tracker.check_aligned takes the block and the block it collided with
                #if no second block - returns False, block1, empty list
                # returns T/F, block1, list of collided/ empty list
            aligned, block, block2 = tracker.check_aligned(block, collided_with)
            if aligned == True:
                    #check_if_sentence returns the blocks
                    #if they are red they will be removed
                if word_logic.check_if_sentence(block, block2):
                    block.color = WHITE
                    block2.color = WHITE

        if block.active == True:
            block.move(change_x, change_y)
        elif block.color == WHITE: #white means its been used to form a sentence
            block.move(0, 1)

        block.draw(screen) # draw all

        game_over = game_functions.is_game_done(block)

    pygame.display.flip() #update view

    clock.tick(30) #limit to 60 frames per second

##### check if game is over function that checks if any inactive blocks are too high

pygame.quit() #End game properly
