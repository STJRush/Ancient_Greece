import pygame as pg
vec = pg.math.Vector2

#colours using the rgb scale
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Ancient Greece"
BGCOLOR = BROWN

TILESIZE = 64

GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'GreenSquare.png'

#Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'survivor1_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
SLING_OFFSET = vec(100, 0)
PLAYER_HEALTH = 400

#Weapon settings
STONE_IMG = 'stone.png'
STONE_SPEED = 500
STONE_LIFETIME = 1000
STONE_RATE = 300
KICKBACK = 200
SLING_SPREAD = 5
STONE_DAMAGE = 20

#Enemy settings
CERBERUS_IMG = 'cerberus.png'
CERBERUS_SPEEDS = [320, 300, 330, 290]
CERBERUS_HIT_RECT = pg.Rect(0, 0, 30, 30)
CERBERUS_HEALTH = 100
CERBERUS_DMG = 10
CERBERUS_KNOCKBACK = 10

#Keeps enemies from stacking on top of each other
AVOID_RADIUS = 50

HYDRA_IMG = 'hydra.png'
HYDRA_SPEEDS = [200, 210, 175, 190]
HYDRA_HIT_RECT = pg.Rect(0, 0, 40, 40)
HYDRA_HEALTH = 200
HYDRA_DMG = 15
HYDRA_KNOCKBACK = 20
