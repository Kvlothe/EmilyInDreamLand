import pygame
import random
from colors import *
import player
from constants import *


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
    return [pygame.Rect(i * player.TERRAIN_WIDTH, terrain_heights[i], player.TERRAIN_WIDTH, player.HEIGHT -
                        terrain_heights[i]) for i in range(len(terrain_heights))]

    # Fixed Terrain
    # fixed_height = int(HEIGHT * 0.75)
    # terrain_length = 100  # Change this number to adjust the terrain length
    # return [pygame.Rect(i * TERRAIN_WIDTH, fixed_height, TERRAIN_WIDTH, HEIGHT - fixed_height) for i in
    #         range(terrain_length)]


def generate_precise_terrain():
    # Define the terrain heights from 0-100. Adjust as needed.
    terrain_heights = [250 for _ in range(0, 15)] + [250 for _ in range(15, 30)] + \
                      [250 for _ in range(30, 35)] + [250 for _ in range(35, 50)] + \
                      [250 for _ in range(50, 65)] + [250 for _ in range(65, 80)] + \
                      [250 for _ in range(80, 95)] + [250 for _ in range(95, 100)]

    # Ensure there are enough colors for each range in the terrain list
    if len(terrain_list) < 8:  # Adjust the number here based on the number of ranges you have
        raise ValueError("Not enough colors defined for the number of terrain ranges")

    # Adjust Y-coordinate to position terrain at the bottom of the screen and assign colors
    terrain_segments = []
    color_ranges = [0, 15, 30, 35, 50, 65, 80, 95, 100]  # Adjust these numbers based on your terrain ranges
    color_index = 0
    for i, height in enumerate(terrain_heights):
        if i == color_ranges[color_index + 1]:
            color_index += 1
        rect = pygame.Rect(i * TERRAIN_WIDTH, HEIGHT - height, TERRAIN_WIDTH, height)
        terrain_segments.append({"rect": rect, "color": terrain_list[color_index]})

    return terrain_segments


def float_blocks():
    floating_blocks = [
        {
            "offset_x": 400,
            "terrain_index": 4,
            "height_above_terrain": 100,
            "color": SIENNA,
            "width": 70,
            "height": 20,
            "type": "floating_block"
         },
        {
            "offset_x": 700,
            "terrain_index": 7,
            "height_above_terrain": 150,
            "color": SIENNA,
            "width": 50,
            "height": 20,
            "type": "floating_block"
        },
        {
            "offset_x": 1200,
            "terrain_index": 10,
            "height_above_terrain": 250,
            "color": SIENNA,
            "width": 70,
            "height": 20,
            "type": "floating_block"
        },
        {
            "offset_x": 1200,
            "terrain_index": 12,
            "height_above_terrain": 350,
            "color": SIENNA,
            "width": 50,
            "height": 20,
            "type": "floating_block"
        },
        {
            "offset_x": 1350,
            "terrain_index": 13,
            "height_above_terrain": 550,
            "color": SIENNA,
            "width": 1500,
            "height": 20,
            "type": "floating_block"
        },
        {
            "offset_x": 3300,
            "terrain_index": 33,
            "height_above_terrain": 250,
            "color": SIENNA,
            "width": 100,
            "height": 20,
            "type": "floating_block"
        },
        {
            "offset_x": 4000,
            "terrain_index": 40,
            "height_above_terrain": 250,
            "color": SIENNA,
            "width": 100,
            "height": 20,
            "type": "floating_block"
        }
        # ... more blocks ...
    ]

    return floating_blocks


def coin_bins():
    coin_bin = [
        # Define each coin box with appropriate properties
        {
            "offset_x": 400,
            "terrain_index": 40,
            "height_above_terrain": 250,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 500,
            "terrain_index": 5,
            "height_above_terrain": 350,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 800,
            "terrain_index": 8,
            "height_above_terrain": 450,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 1300,
            "terrain_index": 13,
            "height_above_terrain": 650,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 1370,
            "terrain_index": 13,
            "height_above_terrain": 750,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 1400,
            "terrain_index": 14,
            "height_above_terrain": 850,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 1550,
            "terrain_index": 15,
            "height_above_terrain": 850,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 1800,
            "terrain_index": 18,
            "height_above_terrain": 850,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 1950,
            "terrain_index": 19,
            "height_above_terrain": 850,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        {
            "offset_x": 2000,
            "terrain_index": 20,
            "height_above_terrain": 650,
            "color": GOLD,
            "width": 50,
            "height": 50,
            "type": "coin_box"
        },
        # Add more coin boxes as needed
    ]
    return coin_bin


def coin_gold():
    gold_coin = [
        # Define each gold coin with appropriate properties
        {
            "offset_x": 1100,
            "terrain_index": 11,
            "height_above_terrain": 450,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 1150,
            "terrain_index": 11,
            "height_above_terrain": 470,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 1180,
            "terrain_index": 11,
            "height_above_terrain": 500,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 1200,
            "terrain_index": 12,
            "height_above_terrain": 520,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 2100,
            "terrain_index": 21,
            "height_above_terrain": 550,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 2130,
            "terrain_index": 22,
            "height_above_terrain": 450,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 2150,
            "terrain_index": 22,
            "height_above_terrain": 410,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 2180,
            "terrain_index": 22,
            "height_above_terrain": 390,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        {
            "offset_x": 2200,
            "terrain_index": 22,
            "height_above_terrain": 350,
            "color": GOLD,
            "width": 10,
            "height": 5,
            "type": "gold_coin"
        },
        # Add more gold coin as needed
    ]
    return gold_coin


def cactus_blocks():
    cactus = [
        {
            "offset_x": 700,
            "terrain_index": 7,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,  # Width of the cactus
            "height": 70,  # Height of the cactus
            "type": "cactus"
        },
        {
            "offset_x": 1200,
            "terrain_index": 12,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 2000,
            "terrain_index": 20,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 3100,
            "terrain_index": 31,
            "height_above_terrain": 150,
            "color": GREEN,
            "width": 30,
            "height": 150,
            "type": "cactus"
        },
        {
            "offset_x": 3300,
            "terrain_index": 33,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 3500,
            "terrain_index": 35,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 4000,
            "terrain_index": 40,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,  # Width of the cactus
            "height": 70, # Height of the cactus
            "type": "cactus"
        },
        {
            "offset_x": 4500,
            "terrain_index": 45,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 5500,
            "terrain_index": 55,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 6000,
            "terrain_index": 60,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 7000,
            "terrain_index": 70,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 8000,
            "terrain_index": 80,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },
        {
            "offset_x": 9000,
            "terrain_index": 90,
            "height_above_terrain": 50,
            "color": GREEN,
            "width": 30,
            "height": 70,
            "type": "cactus"
        },

        # ... add more cactus as needed ...
    ]
    return cactus


# Ground
# GROUND_COLOR = colors.SIENNA
ground_rect = pygame.Rect(0, player.HEIGHT - GROUND_HEIGHT, player.WIDTH, GROUND_HEIGHT)
floating_blocks_color = NAVAJO
