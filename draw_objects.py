# from terrain import *
import pygame

# floating_blocks = float_blocks()
# cactus = cactus_blocks()
# coin_box = coin_bins()
# gold_coin = coin_gold()


def draw_floating_blocks(screen, floating_blocks, terrain, global_position):
    for block_info in floating_blocks:
        terrain_segment = terrain[block_info["terrain_index"]]['rect']
        block_x = terrain_segment.x + block_info["offset_x"] - global_position
        block_y = terrain_segment.y - block_info["height_above_terrain"]
        pygame.draw.rect(screen, block_info["color"], (block_x, block_y, block_info['width'], block_info['height']))


def draw_cacti(screen, cacti, terrain, global_position):
    for cactus_info in cacti:
        terrain_segment = terrain[cactus_info["terrain_index"]]['rect']
        cactus_x = terrain_segment.x + cactus_info["offset_x"] - global_position
        cactus_y = terrain_segment.y - cactus_info["height_above_terrain"]
        pygame.draw.rect(screen, cactus_info["color"], (cactus_x, cactus_y, cactus_info["width"], cactus_info["height"]))


def draw_coin_boxes(screen, coin_box, terrain, global_position):
    # Draw coin boxes
    for coin_info in coin_box:
        terrain_segment = terrain[coin_info["terrain_index"]]['rect']
        coin_x = terrain_segment.x + coin_info["offset_x"] - global_position
        coin_y = terrain_segment.y - coin_info["height_above_terrain"]
        pygame.draw.rect(screen, coin_info["color"], (coin_x, coin_y, coin_info["width"], coin_info["height"]))


def draw_gold_coin(screen, gold_coin, terrain, global_position):
    # Draw gold coins
    for gold_coin_info in gold_coin:
        terrain_segment = terrain[gold_coin_info["terrain_index"]]['rect']
        coin_x = terrain_segment.x + gold_coin_info["offset_x"] - global_position
        coin_y = terrain_segment.y - gold_coin_info["height_above_terrain"]
        pygame.draw.rect(screen, gold_coin_info["color"], (coin_x, coin_y, gold_coin_info["width"], gold_coin_info["height"]))
