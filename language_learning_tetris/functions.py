

blocks = []
all_blocks = pygame.sprite.Group()
landed_blocks = pygame.sprite.Group()


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
