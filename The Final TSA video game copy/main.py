# KidsCanCode - Game Development with Pygame video series
# Tile-based game - Part 2
# Collisions and Tilemaps
# Video link: https://youtu.be/ajR4BZBKTr4
import pygame as pg
import sys
from os import path
from pygame import mixer
from settings import *
from sprites import *
import asyncio
import webbrowser


screen = pygame.display.set_mode((WIDTH, HEIGHT))







   

delay = 100
class Game():
    def __init__(self):
        pg.init()

        self.font = pygame.font.Font("arial.ttf", 32)
        self.fonty = pygame.font.Font("arial.ttf", 16)
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.timer = pg.time.get_ticks()
        self.current_place = 0
        self.places = [0,1]
        self.intro_background = pygame.image.load('introbackground.png')

        
        self.place = self.places[self.current_place]
        
        self.load_data()
        

    

    

    def load_data(self):
        self.files = ['map.txt','map2.txt', 'map3.txt', 'map4.txt'] 
        game_folder = path.dirname(__file__)
        filename =  random.choice(self.files)
        self.map_data = []
        with open(path.join(game_folder, filename), 'rt') as f:
            for line in f:
                self.map_data.append(line)
    


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.secplayers = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.keys = pg.sprite.Group()
        self.beats = pg.sprite.Group()
        
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                        self.player = Player(self, col, row)
                if tile == '2':
                    self.secplayer = SecPlayer(self, col, row)
                if tile == 'K':
                    Key(self, col, row)
                if tile == 'B':
                    Beat(self, col, row)
                if tile == 'C':
                    Boato(self, col, row)
                if tile == 'D':
                    Brato(self, col, row)
                if tile == 'E':
                    Bino(self, col, row)
                                        
    

    def run(self):  
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()


    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

        key_collisons = pg.sprite.spritecollide(self.player, self.keys, False)
        if key_collisons:
            self.load_data()
            self.new()
        key_sec_collisons = pg.sprite.spritecollide(self.secplayer, self.keys, False)
        if key_sec_collisons:
            self.load_data()
            self.new()
        beat_collisons = pg.sprite.groupcollide(self.beats, self.players, False, True)
        if beat_collisons:
            for row, tiles in enumerate(self.map_data):
                for col, tile in enumerate(tiles):
               	    if tile == 'P':
                        self.player = Player(self, col, row)
        beat_sec_collisons = pg.sprite.groupcollide(self.beats, self.secplayers, False, True)
        if beat_sec_collisons:
            for row, tiles in enumerate(self.map_data):
                for col, tile in enumerate(tiles):
               	    if tile == '2':
                        self.secplayer = SecPlayer(self, col, row)
        
        

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        
        pg.display.flip()
    def events(self,delay=100):
        # catch all events here
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)          
                if event.key == pg.K_a:
                    self.secplayer.move(dx=-1)
                if event.key == pg.K_d:
                    self.secplayer.move(dx=1)
                if event.key == pg.K_w:
                    self.secplayer.move(dy=-1)
                if event.key == pg.K_s :
                    self.secplayer.move(dy=1)  

    


    def intro_screen(self):
        intro = True

        title = self.font.render('Color Runner', True, BLACK)
        title_rect = title .get_rect(x=10, y=10)
        paragraph = self.fonty.render('Hello, My Name is Amari Owens and I have submitted a party maze game that works will one player moving ', True, BLACK)
        paragraph_two = self.fonty.render(' to the center of the screen. The goal is to get to big red square at the bottom of the map. Only the player can  ', True, BLACK)
        paragraph_three = self.fonty.render('reach the center. Move to the when you see the white square. P1 uses the arrow keys. P2 uses the WASD',True, BLACK)
        paragraph_rect = title.get_rect(x=0, y =100)
        paragraph_rect_two = title.get_rect(x=0, y=120)
        paragraph_rect_three = title.get_rect(x=0, y=140)
        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(paragraph, paragraph_rect)
            self.screen.blit(paragraph_two, paragraph_rect_two)
            self.screen.blit(paragraph_three, paragraph_rect_three)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def show_go_screen(self):
        pass



g = Game()
colors = [RED, WHITE]
current_color = 0

color = colors[current_color]
timer = pygame.time.get_ticks()

async def main():
   
 

    while True:
        g.intro_screen()
        g.new()
        g.run()
        g.show_go_screen()
        k = pygame.key.get_pressed()
    
   

asyncio.run(main())




    #now we will loop through the keys and handle the events
   
    
    

# create the game object
    

    