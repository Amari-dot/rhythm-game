import pygame 
from settings import *
from pygame import mixer
import random
import sys
mixer.init()
pygame.init()


import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.xchange = 0
        self.ychange = 0
        self.direction = None 

    
    def move(self, dx=0, dy=0):
        for keys in self.game.keys:
            if keys.color == (255,255,255):
                
                if not self.collide_with_walls(dx, dy):
                    self.is_collide_with_keys()
                    self.x += dx 
                    self.y += dy
                    self.direction = (dx, dy)
        self.xchange =  dx 
        self.ychange =  dy            
            

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    def is_collide_with_keys(self, dx=0, dy=0):
        for key in self.game.keys:
            if  key.x == self.x + dx and key.y - dy == self.y:
                print("I'm am touching the key")
                self.kill()

                return True
        return False
    
    
    def distancechanged(self,dx=0,dy=0):
        if self.x + dx < 2 or self.x - dx > -2 or self.y + dy < 2 or self.y - dy > -2:
            return True
        return False

    def ontime(self):
        for key in self.game.keys:
            if key.color == (255,255,255):
                print("ontime")
                
            
            

    def update(self):

        
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
class SecPlayer(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.secplayers
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.xchange = 0
        self.ychange = 0
        self.direction = None 

    
    def move(self, dx=0, dy=0):
        for keys in self.game.keys:
            if keys.color == (255,255,255):
                
                if not self.collide_with_walls(dx, dy):
                    self.is_collide_with_keys()
                    self.x += dx 
                    self.y += dy
                    self.direction = (dx, dy)
        self.xchange =  dx 
        self.ychange =  dy            
            

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
    def is_collide_with_keys(self, dx=0, dy=0):
        for key in self.game.keys:
            if  key.x == self.x + dx and key.y - dy == self.y:
                print("I'm am touching the key")
                self.kill()

                return True
        return False
    
    
    def distancechanged(self,dx=0,dy=0):
        if self.x + dx < 2 or self.x - dx > -2 or self.y + dy < 2 or self.y - dy > -2:
            return True
        return False

    def ontime(self):
        for key in self.game.keys:
            if key.color == (255,255,255):
                print("ontime")
                
            
            

    def update(self):

        
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

        
        

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


current_time = 0
button_press_time= 0   
#self.rect = pygame.Rect(self.x,self.y,100,40)

class Key(pygame.sprite.Sprite):


    def __init__(self,game,x,y, colors=None):
        super().__init__()
        
        self.groups = game.all_sprites, game.keys
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.handled = False
        self.colors = [RED, WHITE]

        self.current_color = 0


        self.color = self.colors[self.current_color]
        self.timer = pygame.time.get_ticks()
 
    
    def update(self):
        
        self.animate()
        
        
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    
    
    def animate(self, delay=400):
        if pygame.time.get_ticks() - self.timer > delay:
            self.timer = pygame.time.get_ticks()
            
            
            self.current_color = (self.current_color + 1) % len(self.colors)
            self.color = self.colors[self.current_color]
            self.image.fill(self.color)
            self.has_been_handled()
            
            
              
        

    
    def has_been_handled(self):
        
        return self.handled
        


class Beat(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.beats
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.timing = pygame.time.Clock()
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.movement_loop = 0
        self.max_travel = 12
        self.x = x
        self.y = y
        self.timer = pygame.time.get_ticks()
        
    
    def move(self, dx=0, dy=0, delay=200):
        if pygame.time.get_ticks() - self.timer > delay:
            self.timer = pygame.time.get_ticks()
            self.movement_loop += 1
            
            if self.movement_loop <= 13:
                self.x -= dx
            elif self.movement_loop <= 26:
                self.x += dx
        
            if self.movement_loop == 26:
                self.movement_loop = 0


    def collide_with_keys(self, dx=0, dy=0):
        for key in self.game.keys:
            if key.x == self.x - dx and key.y == self.y + dy:
                self.kill()

                return True
                
        return False


        

    def update(self):
        self.move(dx=1)

        
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
class Boato(Beat):
    def __init__(self, game, x, y):
        super().__init__(game, x, y)

    def move(self, dx=0, dy=0, delay=200):
        if pygame.time.get_ticks() - self.timer > delay:
            self.timer = pygame.time.get_ticks()
            self.movement_loop += 1
            
            if self.movement_loop <= 13:
                self.x += dx
            elif self.movement_loop <= 26:
                self.x -= dx
        
            if self.movement_loop == 26:
                self.movement_loop = 0    
class Brato(Beat):
        def __init__(self, game, x, y):
            super().__init__(game, x, y)
            self.image.fill(PURPLE)

        def move(self, dx=0, dy=0, delay=900):
            if pygame.time.get_ticks() - self.timer > delay:
                self.timer = pygame.time.get_ticks()
                self.movement_loop += 1
                
                if self.movement_loop <= 13:
                    self.x -= dx
                elif self.movement_loop <= 26:
                    self.x += dx
            
                if self.movement_loop == 26:
                    self.movement_loop = 0   
class Bino(Beat):
        def __init__(self, game, x, y):
            super().__init__(game, x, y)
            self.image.fill(PURPLE)

        def move(self, dx=0, dy=0, delay=900):
            if pygame.time.get_ticks() - self.timer > delay:
                self.timer = pygame.time.get_ticks()
                self.movement_loop += 1
                
                if self.movement_loop <= 13:
                    self.x += dx
                elif self.movement_loop <= 26:
                    self.x -= dx
            
                if self.movement_loop == 26:
                    self.movement_loop = 0  

class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('arial.ttf', fontsize)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height 

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False


pygame.quit()