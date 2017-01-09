import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, word, color, font_color):
        pygame.sprite.Sprite.__init__(self)
        #self.id = this_id
        self.x = 275
        self.y = 0
        self.word = word
        self.change_x = 0
        self.change_y = 0
        self.color = color
        self.test = False
        self.font_color = font_color
        self.active = True
        self.image = pygame.Surface((100,50))
        self.rect = self.image.get_rect()

        #self.landed = False
    def move(self, change_x, change_y):
        #if self.active == True:
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
        #else:
        #    self.x = self.x
        #    self.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen,self.color,[self.x,self.y,100,50],0)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(self.word,True,self.font_color)
        screen.blit(text, [self.x+15, self.y+15])

    def check(self, landed_blocks):
        if self.active == True:
            if self.y >= 450:
                self.active = False
                self.test = True
                #self.landed = True
                landed_blocks.add(self)
            elif pygame.sprite.spritecollideany(self, landed_blocks, False):
                collided = pygame.sprite.spritecollide(self, landed_blocks, False)
                for block in collided:
                    self.check_aligned(block)
                print 'collision'
                self.active = False
                #self.landed = True
                landed_blocks.add(self)
            return landed_blocks


    def check_aligned(self,block2):
        if abs(self.x - block2.x) < 25 or (self.x + 100) == block2.x:
            print 'words', self.word, block2.word
            for sentence in sentences:
                if sentence[0] == self.word and sentence[1] == block2.word:
                    self.color = RED
                    block2.color = RED
                    self.y = 500
                    block2.y = 500
