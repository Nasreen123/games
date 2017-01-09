import pygame

def check(block, landed_blocks):
    if block.active == True:
        if block.y >= 450 and pygame.sprite.spritecollideany(block, landed_blocks, False) == False:
            block.active = False
            block.test = True
            #self.landed = True
            landed_blocks.add(block)
            return (block, landed_blocks, False, [block])
        elif pygame.sprite.spritecollideany(block, landed_blocks, False) == True:
            collided = pygame.sprite.spritecollide(block, landed_blocks, False)
            for each_block in collided:
                block.check_aligned(each_block)
            block.active = False
            #self.landed = True
            landed_blocks.add(block)
            return (landed_blocks, True, collided)
    else:
        return (block, landed_blocks, False, [cblock])




def check_aligned(block1,block2):
    if abs(block1.x - block2.x) < 25 or (self.x + 100) == block2.x:
        print 'words', block1.word, block2.word
        for sentence in sentences:
            if sentence[0] == block1.word and sentence[1] == block2.word:
                block1.color = RED
                block2.color = RED
                block1.y = 500
                block2.y = 500
