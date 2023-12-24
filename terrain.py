import pygame
import random
from colors import *
import player
from constants import *


def generate_terrain_height():
    return random.randint(int(player.HEIGHT * 0.5), int(player.HEIGHT * 0.75))


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
    terrain_heights = [100 for _ in range(0, 15)] + [100 for _ in range(15, 30)] + \
                      [100 for _ in range(30, 35)] + [100 for _ in range(35, 50)] + \
                      [100 for _ in range(50, 65)] + [100 for _ in range(65, 80)] + \
                      [100 for _ in range(80, 95)] + [100 for _ in range(95, 100)]

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
            "offset_x": 50, "terrain_index": 0, "height_above_terrain": 200, "color": BLUE, "width": 70,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 50, "terrain_index": 0, "height_above_terrain": 400, "color": BLUE, "width": 70,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 50, "terrain_index": 0, "height_above_terrain": 600, "color": BLUE, "width": 70,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 400, "terrain_index": 4, "height_above_terrain": 100, "color": SIENNA, "width": 70,
            "height": 20, "type": "floating_block"
         },
        {
            "offset_x": 700, "terrain_index": 7, "height_above_terrain": 150, "color": SIENNA, "width": 50,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 1200, "terrain_index": 10, "height_above_terrain": 250, "color": SIENNA, "width": 70,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 1200, "terrain_index": 12, "height_above_terrain": 350, "color": SIENNA, "width": 50,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 1350, "terrain_index": 13, "height_above_terrain": 550, "color": SIENNA, "width": 1500,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 3300, "terrain_index": 33, "height_above_terrain": 250, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 4000, "terrain_index": 40, "height_above_terrain": 250, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 4300, "terrain_index": 43, "height_above_terrain": 250, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 4400, "terrain_index": 44, "height_above_terrain": 350, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 4500, "terrain_index": 45, "height_above_terrain": 450, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 4600, "terrain_index": 46, "height_above_terrain": 550, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 4700, "terrain_index": 47, "height_above_terrain": 650, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 4800, "terrain_index": 48, "height_above_terrain": 750, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 5000, "terrain_index": 50, "height_above_terrain": 750, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 5200, "terrain_index": 52, "height_above_terrain": 750, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 5500, "terrain_index": 55, "height_above_terrain": 450, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 5600, "terrain_index": 56, "height_above_terrain": 650, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 6600, "terrain_index": 66, "height_above_terrain": 250, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 6700, "terrain_index": 67, "height_above_terrain": 350, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7000, "terrain_index": 70, "height_above_terrain": 350, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7200, "terrain_index": 72, "height_above_terrain": 250, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7250, "terrain_index": 73, "height_above_terrain": 450, "color": BLUE, "width": 20,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7400, "terrain_index": 74, "height_above_terrain": 550, "color": SIENNA, "width": 300,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7500, "terrain_index": 75, "height_above_terrain": 550, "color": SIENNA, "width": 20,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7700, "terrain_index": 77, "height_above_terrain": 550, "color": SIENNA, "width": 20,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7400, "terrain_index": 74, "height_above_terrain": 250, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7800, "terrain_index": 78, "height_above_terrain": 650, "color": SIENNA, "width": 300,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 8050, "terrain_index": 80, "height_above_terrain": 650, "color": SIENNA, "width": 20,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 8150, "terrain_index": 81, "height_above_terrain": 650, "color": SIENNA, "width": 20,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7600, "terrain_index": 76, "height_above_terrain": 250, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 8200, "terrain_index": 82, "height_above_terrain": 750, "color": SIENNA, "width": 500,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7800, "terrain_index": 78, "height_above_terrain": 150, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 8000, "terrain_index": 80, "height_above_terrain": 200, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 8200, "terrain_index": 82, "height_above_terrain": 150, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 7400, "terrain_index": 84, "height_above_terrain": 100, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 8600, "terrain_index": 86, "height_above_terrain": 150, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 8800, "terrain_index": 88, "height_above_terrain": 200, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        {
            "offset_x": 9000, "terrain_index": 90, "height_above_terrain": 150, "color": SIENNA, "width": 100,
            "height": 20, "type": "floating_block"
        },
        # {
        #     "offset_x": 100, "terrain_index": 92, "height_above_terrain": 250, "color": SIENNA, "width": 300,
        #     "height": 20, "type": "floating_block"
        # },
        # {
        #     "offset_x": 100, "terrain_index": 94, "height_above_terrain": 350, "color": SIENNA, "width": 100,
        #     "height": 20, "type": "floating_block"
        # },
        # {
        #     "offset_x": 100, "terrain_index": 96, "height_above_terrain": 450, "color": SIENNA, "width": 100,
        #     "height": 20, "type": "floating_block"
        # },
        # {
        #     "offset_x": 9800, "terrain_index": 98, "height_above_terrain": 550, "color": SIENNA, "width": 300,
        #     "height": 20, "type": "floating_block"
        # },
        # {
        #     "offset_x": 9900, "terrain_index": 99, "height_above_terrain": 150, "color": SIENNA, "width": 100,
        #     "height": 20, "type": "floating_block"
        # },
    ]

    return floating_blocks


def coin_bins():
    coin_bin = [
        # {
        #     "offset_x": 0, "terrain_index": 1, "height_above_terrain": 50, "color": GOLD, "width": 50,
        #     "height": 50, "type": "coin_box"
        # },
        # {
        #     "offset_x": 100, "terrain_index": 2, "height_above_terrain": 50, "color": GOLD, "width": 50,
        #     "height": 50, "type": "coin_box"
        # },
        # {
        #     "offset_x": 0, "terrain_index": 3, "height_above_terrain": 50, "color": GOLD, "width": 50,
        #     "height": 50, "type": "coin_box"
        # },
        {
            "offset_x": 50, "terrain_index": 0, "height_above_terrain": 250, "color": BLUE, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 50, "terrain_index": 0, "height_above_terrain": 450, "color": BLUE, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 50, "terrain_index": 0, "height_above_terrain": 650, "color": BLUE, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 70, "terrain_index": 0, "height_above_terrain": 250, "color": BLUE, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 70, "terrain_index": 0, "height_above_terrain": 450, "color": BLUE, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 70, "terrain_index": 0, "height_above_terrain": 650, "color": BLUE, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 400, "terrain_index": 40, "height_above_terrain": 250, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 500, "terrain_index": 5, "height_above_terrain": 300, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 800, "terrain_index": 8, "height_above_terrain": 400, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 1350, "terrain_index": 13, "height_above_terrain": 670, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 1390, "terrain_index": 13, "height_above_terrain": 800, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 1400, "terrain_index": 14, "height_above_terrain": 850, "color": GOLD, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 1550, "terrain_index": 15, "height_above_terrain": 850, "color": GOLD, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 1800, "terrain_index": 18, "height_above_terrain": 850, "color": GOLD, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 1950, "terrain_index": 19, "height_above_terrain": 850, "color": GOLD, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 2000, "terrain_index": 20, "height_above_terrain": 650, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 3130, "terrain_index": 31, "height_above_terrain": 50, "color": BLUE, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 4800, "terrain_index": 48, "height_above_terrain": 850, "color": GOLD, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 5000, "terrain_index": 50, "height_above_terrain": 850, "color": GOLD, "width": 50,
            "height": 50, "type": "coin_box"
        },
        {
            "offset_x": 8000, "terrain_index": 80, "height_above_terrain": 350, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 8200, "terrain_index": 82, "height_above_terrain": 800, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 8300, "terrain_index": 83, "height_above_terrain": 850, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 8400, "terrain_index": 84, "height_above_terrain": 800, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 8500, "terrain_index": 85, "height_above_terrain": 850, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 8200, "terrain_index": 82, "height_above_terrain": 300, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 7400, "terrain_index": 84, "height_above_terrain": 250, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 8600, "terrain_index": 86, "height_above_terrain": 300, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 8800, "terrain_index": 88, "height_above_terrain": 350, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        {
            "offset_x": 9000, "terrain_index": 90, "height_above_terrain": 300, "color": GOLD, "width": 30,
            "height": 30, "type": "coin_box"
        },
        # {
        #     "offset_x": 9200, "terrain_index": 92, "height_above_terrain": 350, "color": GOLD, "width": 50,
        #     "height": 50, "type": "coin_box"
        # },
        # {
        #     "offset_x": 9400, "terrain_index": 94, "height_above_terrain": 450, "color": GOLD, "width": 50,
        #     "height": 50, "type": "coin_box"
        # },
        # {
        #     "offset_x": 9600, "terrain_index": 96, "height_above_terrain": 550, "color": GOLD, "width": 50,
        #     "height": 50, "type": "coin_box"
        # },
        # {
        #     "offset_x": 9800, "terrain_index": 98, "height_above_terrain": 650, "color": GOLD, "width": 50,
        #     "height": 50, "type": "coin_box"
        # },
        # Add more coin boxes as needed
    ]
    return coin_bin


def coin_gold():
    gold_coin = [
        {
            "offset_x": 190, "terrain_index": 2, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 220, "terrain_index": 2, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 240, "terrain_index": 2, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 280, "terrain_index": 2, "height_above_terrain": 250, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 220, "terrain_index": 3, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 260, "terrain_index": 3, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 280, "terrain_index": 3, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 1100, "terrain_index": 11, "height_above_terrain": 450, "color": SILVER,  "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 1150, "terrain_index": 11, "height_above_terrain": 470, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 1180, "terrain_index": 11, "height_above_terrain": 500, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 1200, "terrain_index": 12, "height_above_terrain": 520, "color": SILVER,  "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2100, "terrain_index": 21, "height_above_terrain": 550, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2130, "terrain_index": 22, "height_above_terrain": 450, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2150, "terrain_index": 22, "height_above_terrain": 410, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2180, "terrain_index": 22, "height_above_terrain": 390, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2200, "terrain_index": 22, "height_above_terrain": 350, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2300, "terrain_index": 23, "height_above_terrain": 150, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2450, "terrain_index": 24, "height_above_terrain": 110, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2500, "terrain_index": 25, "height_above_terrain": 90, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2600, "terrain_index": 26, "height_above_terrain": 200, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2700, "terrain_index": 27, "height_above_terrain": 150, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2800, "terrain_index": 28, "height_above_terrain": 110, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2900, "terrain_index": 29, "height_above_terrain": 90, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 2950, "terrain_index": 29, "height_above_terrain": 200, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3000, "terrain_index": 30, "height_above_terrain": 150, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3050, "terrain_index": 30, "height_above_terrain": 110, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3100, "terrain_index": 31, "height_above_terrain": 200, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3150, "terrain_index": 31, "height_above_terrain": 200, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3600, "terrain_index": 36, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3620, "terrain_index": 36, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3640, "terrain_index": 36, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3680, "terrain_index": 36, "height_above_terrain": 250, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3620, "terrain_index": 37, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3640, "terrain_index": 37, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3660, "terrain_index": 37, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3800, "terrain_index": 38, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3820, "terrain_index": 38, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3840, "terrain_index": 38, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3880, "terrain_index": 38, "height_above_terrain": 250, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3820, "terrain_index": 39, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3840, "terrain_index": 39, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 3860, "terrain_index": 39, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 4000, "terrain_index": 40, "height_above_terrain": 300, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 4300, "terrain_index": 43, "height_above_terrain": 300, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 4400, "terrain_index": 44, "height_above_terrain": 400, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 4500, "terrain_index": 45, "height_above_terrain": 500, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 4600, "terrain_index": 46, "height_above_terrain": 800, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 4700, "terrain_index": 47, "height_above_terrain": 700, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6200, "terrain_index": 62, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6220, "terrain_index": 62, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6240, "terrain_index": 62, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6280, "terrain_index": 62, "height_above_terrain": 250, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6220, "terrain_index": 63, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6240, "terrain_index": 63, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6260, "terrain_index": 63, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6400, "terrain_index": 64, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6420, "terrain_index": 64, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6440, "terrain_index": 64, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6480, "terrain_index": 64, "height_above_terrain": 250, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6420, "terrain_index": 65, "height_above_terrain": 220, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6440, "terrain_index": 65, "height_above_terrain": 180, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 6460, "terrain_index": 65, "height_above_terrain": 150, "color": GOLD, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7400, "terrain_index": 74, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7450, "terrain_index": 74, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7500, "terrain_index": 75, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7550, "terrain_index": 75, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7600, "terrain_index": 76, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7650, "terrain_index": 76, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7700, "terrain_index": 77, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
        {
            "offset_x": 7750, "terrain_index": 77, "height_above_terrain": 580, "color": SILVER, "width": 10,
            "height": 5, "type": "gold_coin"
        },
    ]
    return gold_coin


def cactus_blocks():
    cactus = [
        {
            "offset_x": 700, "terrain_index": 7, "height_above_terrain": 50, "color": GREEN, "width": 50,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1200, "terrain_index": 12, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1300, "terrain_index": 13, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1350, "terrain_index": 13, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1400, "terrain_index": 14, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1450, "terrain_index": 14, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1500, "terrain_index": 15, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1550, "terrain_index": 15, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1600, "terrain_index": 16, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1650, "terrain_index": 16, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1700, "terrain_index": 17, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1750, "terrain_index": 17, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1800, "terrain_index": 18, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1850, "terrain_index": 18, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1900, "terrain_index": 19, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 1950, "terrain_index": 19, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 2000, "terrain_index": 20, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 2050, "terrain_index": 20, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 2100, "terrain_index": 21, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 2150, "terrain_index": 21, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 2200, "terrain_index": 22, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 2550, "terrain_index": 25, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 2650, "terrain_index": 26, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 2700, "terrain_index": 27, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 2800, "terrain_index": 28, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 3000, "terrain_index": 30, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 3100, "terrain_index": 31, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 3300, "terrain_index": 33, "height_above_terrain": 50, "color": GREEN, "width": 50,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 3500, "terrain_index": 35, "height_above_terrain": 50, "color": GREEN, "width": 50,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 4000, "terrain_index": 40, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 4150, "terrain_index": 41, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 4300, "terrain_index": 43, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 4450, "terrain_index": 44, "height_above_terrain": 150, "color": GREEN, "width": 40,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 4500, "terrain_index": 45, "height_above_terrain": 30, "color": GREEN, "width": 70,
            "height": 40, "type": "cactus"
        },
        {
            "offset_x": 4650, "terrain_index": 46, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 4850, "terrain_index": 48, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 4900, "terrain_index": 49, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 5000, "terrain_index": 50, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 5100, "terrain_index": 51, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 5150, "terrain_index": 51, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 5250, "terrain_index": 52, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 5300, "terrain_index": 53, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 5450, "terrain_index": 54, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 5550, "terrain_index": 55, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 5600, "terrain_index": 56, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 5700, "terrain_index": 57, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 5850, "terrain_index": 58, "height_above_terrain": 150, "color": GREEN, "width": 30,
            "height": 150, "type": "cactus"
        },
        {
            "offset_x": 5900, "terrain_index": 59, "height_above_terrain": 50, "color": GREEN, "width": 70,
            "height": 30, "type": "cactus"
        },
        {
            "offset_x": 5950, "terrain_index": 59, "height_above_terrain": 50, "color": GREEN, "width": 70,
            "height": 30, "type": "cactus"
        },
        {
            "offset_x": 6000, "terrain_index": 60, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 7000, "terrain_index": 70, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 7500, "terrain_index": 75, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 8000, "terrain_index": 80, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 8300, "terrain_index": 83, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 8800, "terrain_index": 88, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 9000, "terrain_index": 90, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },
        {
            "offset_x": 9500, "terrain_index": 95, "height_above_terrain": 50, "color": GREEN, "width": 30,
            "height": 70, "type": "cactus"
        },

        # ... add more cactus as needed ...
    ]
    return cactus


# Ground
# GROUND_COLOR = colors.SIENNA
# ground_rect = pygame.Rect(0, player.HEIGHT - GROUND_HEIGHT, player.WIDTH, GROUND_HEIGHT)
# floating_blocks_color = NAVAJO
