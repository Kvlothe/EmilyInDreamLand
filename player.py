import colors
import pygame
from constraints import *


def reset_player():
    global player_pos, vy
    player_pos = [0, 460]
    vy = 0


# Player
# player_pos = [WIDTH / 2, HEIGHT / 2 - 50]
# player_pos = [0, 460]
player_size = (30, 40)
player_color = colors.PINK
vy = 0  # vertical speed
on_ground = False
global_position = 0
player_images = [pygame.image.load('walk/walk0.png'), pygame.image.load('walk/walk1.png'),
                 pygame.image.load('walk/walk2.png'), pygame.image.load('walk/walk3.png'),
                 pygame.image.load('walk/walk4.png'), pygame.image.load('walk/walk5.png'),
                 pygame.image.load('walk/walk6.png'), pygame.image.load('walk/walk7.png'),
                 pygame.image.load('walk/walk8.png'), pygame.image.load('walk/walk9.png')]

current_frame = 0
FRAME_DURATION = 5  # number of game loops a single frame lasts for
frame_counter = 0  # counts loops to determine when to switch frames


SPRITE_WIDTH = 140  # example width
SPRITE_HEIGHT = 160  # example height

player_images = [pygame.transform.scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in player_images]
player_pos = [50, HEIGHT - SPRITE_HEIGHT - GROUND_HEIGHT]
player_rect = pygame.Rect(player_pos[0], player_pos[1], SPRITE_WIDTH, SPRITE_HEIGHT)
