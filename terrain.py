import pygame
import random
import colors
import player
from constraints import *


def generate_terrain_height():
    return random.randint(int(player.HEIGHT * 0.5), int(player.HEIGHT * 0.75))


TERRAIN_LENGTH = 100  # The total number of terrain segments


def generate_terrain():
    # Terrain
    terrain_heights = [450, 340, 330, 320, 430, 440, 450, 460,
                       450, 440, 430, 420, 430, 440, 450, 460,
                       550, 540, 530, 700, 530, 700, 550, 560,
                       450, 350, 350, 320, 430, 460, 450, 460,
                       450, 440, 430, 420, 430, 440, 450, 460,
                       550, 700, 530, 700, 700, 700, 450, 460]
    return [pygame.Rect(i * player.TERRAIN_WIDTH, terrain_heights[i], player.TERRAIN_WIDTH, player.HEIGHT - terrain_heights[i]) for i in
            range(len(terrain_heights))]

    # Fixed Terrain
    # fixed_height = int(HEIGHT * 0.75)
    # terrain_length = 100  # Change this number to adjust the terrain length
    # return [pygame.Rect(i * TERRAIN_WIDTH, fixed_height, TERRAIN_WIDTH, HEIGHT - fixed_height) for i in
    #         range(terrain_length)]


def generate_precise_terrain():
    # Define the terrain heights from 0-100. Adjust as needed.
    terrain_heights = [450 for _ in range(0, 15)] + [440 for _ in range(15, 30)] + \
                      [400 for _ in range(30, 35)] + [460 for _ in range(35, 50)] + \
                      [420 for _ in range(50, 65)] + [480 for _ in range(65, 80)] + \
                      [450 for _ in range(80, 95)] + [410 for _ in range(95, 100)]

    return [pygame.Rect(i * player.TERRAIN_WIDTH, terrain_heights[i], player.TERRAIN_WIDTH, player.HEIGHT - terrain_heights[i]) for i in
            range(TERRAIN_LENGTH)]


def float_blocks():
    # Floating blocks list
    floating_blocks = [
        pygame.Rect(300, 350, 70, 20),   # x, y, width, height
        pygame.Rect(500, 250, 70, 20),   # Another block
        # ... Add more blocks as needed
    ]
    floating_blocks_color = colors.NAVAJO
    return floating_blocks


# Ground
GROUND_COLOR = colors.SIENNA
ground_rect = pygame.Rect(0, player.HEIGHT - GROUND_HEIGHT, player.WIDTH, GROUND_HEIGHT)
