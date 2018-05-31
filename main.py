#PADRAIG'S CODE BEGINS
#Tutorals by Kidscancode
#Imports
import pygame as pg
import sys
from os import path
#imports everything from other python files
from settings import *
from sprites import *
from tilemap import *

#ENTIRE GAME 
class Game:
    #initialize the class
    def __init__(self):
        pg.init()
        #Variables arw anything in all CAPS
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
#Loads images
    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img2')
        #map_folder = path.join(game_folder, 'maps')
        self.map = Map(path.join(game_folder, 'map3.txt'))
        #self.map_image = self.map.make_map()
        #self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.stone_img = pg.image.load(path.join(img_folder, STONE_IMG)).convert_alpha()
        self.cerberus_img = pg.image.load(path.join(img_folder, CERBERUS_IMG)).convert_alpha()
        self.hydra_img = pg.image.load(path.join(img_folder, HYDRA_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.stones = pg.sprite.Group()
        # Tells the program to put specific things on the map
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'C':
                    Cerberus(self, col, row)
                if tile == 'H':
                    Hydra(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
        #self.player = Player(self, 5, 5)
        self.camera = Camera(self.map.width, self.map.height)

     #function for running the code
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0
            self.events()
            self.update()
            self.draw()
    #Quit program once player closes window
    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        # mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= HYDRA_DMG
            self.player.health -= CERBERUS_DMG
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(CERBERUS_KNOCKBACK, 0).rotate(-hits[0].rot)
            self.player.pos += vec(HYDRA_KNOCKBACK, 0).rotate(-hits[0].rot)
          #if stones hit enemies
        hits = pg.sprite.groupcollide(self.mobs, self.stones, False, True)
        for hit in hits:
            hit.health -= STONE_DAMAGE
            hit.vel - vec(0, 0)
    #Draw the grid on the map
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    #Draw everything
    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)
        #self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Hydra) or isinstance(sprite, Cerberus) or isinstance(sprite, Player):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()
    #If a player clicks or presses something
    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
    #PASS means leave it for now
    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
