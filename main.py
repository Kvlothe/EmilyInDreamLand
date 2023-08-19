import pygame
from pygame.locals import *
import random
import colors


def generate_terrain_height():
    return random.randint(int(HEIGHT * 0.5), int(HEIGHT * 0.75))


TERRAIN_LENGTH = 100  # The total number of terrain segments


def generate_terrain():
    # Terrain
    terrain_heights = [450, 340, 330, 320, 430, 440, 450, 460,
                       450, 440, 430, 420, 430, 440, 450, 460,
                       550, 540, 530, 700, 530, 700, 550, 560,
                       450, 350, 350, 320, 430, 460, 450, 460,
                       450, 440, 430, 420, 430, 440, 450, 460,
                       550, 700, 530, 700, 700, 700, 450, 460]
    return [pygame.Rect(i * TERRAIN_WIDTH, terrain_heights[i], TERRAIN_WIDTH, HEIGHT - terrain_heights[i]) for i in
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

    return [pygame.Rect(i * TERRAIN_WIDTH, terrain_heights[i], TERRAIN_WIDTH, HEIGHT - terrain_heights[i]) for i in
            range(TERRAIN_LENGTH)]


# Floating blocks list
floating_blocks = [
    pygame.Rect(300, 350, 70, 20),   # x, y, width, height
    pygame.Rect(500, 250, 70, 20),   # Another block
    # ... Add more blocks as needed
]
floating_blocks_color = colors.NAVAJO


def reset_player():
    global player_pos, vy
    player_pos = [0, 460]
    vy = 0


# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
GRAVITY = 0.5
JUMP_STRENGTH = -15
SCROLL_SPEED = 5
TERRAIN_WIDTH = 100
LEFT_SCROLL_THRESHOLD = WIDTH * 0.25  # This means the screen starts scrolling when the player is 25% from the left edge
RIGHT_SCROLL_THRESHOLD = WIDTH * 0.75


# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emily in Dreamland")
clock = pygame.time.Clock()


terrain = generate_precise_terrain()

current_segment_index = len(terrain) - 1


# Define end flag after the last terrain segment
flag_width, flag_height = 50, 150
flag_pos = [terrain[-1].right, terrain[-1].top - flag_height]
end_flag = pygame.Rect(flag_pos[0], flag_pos[1], flag_width, flag_height)


# Player
# player_pos = [WIDTH / 2, HEIGHT / 2 - 50]
player_pos = [0, 460]
player_size = (30, 40)
player_color = colors.PINK
vy = 0  # vertical speed
on_ground = False
global_position = 0
# player_images = [pygame.image.load('walk0.png'), pygame.image.load('walk1.png'),
#                  pygame.image.load('walk2.png'), pygame.image.load('walk3.png'),
#                  pygame.image.load('walk4.png'), pygame.image.load('walk5.png'),
#                  pygame.image.load('walk6.png'), pygame.image.load('walk7.png'),
#                  pygame.image.load('walk8.png'), pygame.image.load('walk9.png')]

# current_frame = 0
# FRAME_DURATION = 5  # number of game loops a single frame lasts for
# frame_counter = 0  # counts loops to determine when to switch frames

# Ground
GROUND_HEIGHT = 100
GROUND_COLOR = colors.SIENNA
ground_rect = pygame.Rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT)

SPRITE_WIDTH = 140  # example width
SPRITE_HEIGHT = 160  # example height

# player_images = [pygame.transform.scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in player_images]
# player_pos = [50, HEIGHT - SPRITE_HEIGHT - GROUND_HEIGHT]

running = True
while running:
    screen.fill(colors.BLUE)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # frame_counter += 1
    # if frame_counter >= FRAME_DURATION:
    #     frame_counter = 0
    #     current_frame = (current_frame + 1) % len(player_images)

    if keys[K_RIGHT]:
        for block in floating_blocks:  # This line and the next ensure the blocks remain static on the screen
            block.move_ip(SCROLL_SPEED, 0)
        # Check the height of the next terrain segment compared to the current position of the player.
        current_terrain = None
        next_terrain = None
        for i, segment in enumerate(terrain):
            if player_pos[0] + player_size[0] > segment.left and player_pos[0] < segment.right:
                current_terrain = segment
                if i + 1 < len(terrain):
                    next_terrain = terrain[i + 1]
                break

        can_move_right = True
        if next_terrain and current_terrain:
            potential_player_rect = pygame.Rect(player_pos[0] + PLAYER_SPEED, player_pos[1], *player_size)

            if next_terrain and potential_player_rect.colliderect(next_terrain):
                # Here we detected a potential collision if the player moves right.
                can_move_right = False

        # If player reaches the middle of the screen
        if player_pos[0] >= RIGHT_SCROLL_THRESHOLD:
            global_position += SCROLL_SPEED
            end_flag.move_ip(-SCROLL_SPEED, 0)
            if can_move_right or not on_ground:  # Allow right movement if player is in the air
                for segment in terrain:
                    segment.move_ip(-SCROLL_SPEED, 0)

                # Add new terrain on the right
                if terrain[-1].right < WIDTH:
                    # Check if there's more terrain in terrain_heights to add
                    if current_segment_index + 1 < len(terrain):
                        current_segment_index += 1
                        new_height = terrain
                        [current_segment_index]
                        new_segment = pygame.Rect(terrain[-1].right, new_height, TERRAIN_WIDTH, HEIGHT - new_height)
                        terrain.append(new_segment)
            elif on_ground:
                # If on ground and can't move right, push the player back slightly
                player_pos[0] -= PLAYER_SPEED

        # Otherwise, the player moves to the right as usual
        else:
            if can_move_right or not on_ground:  # Allow the player to move right if they are in the air
                player_pos[0] += PLAYER_SPEED

    # If the player's position is at the starting point, they shouldn't move further left
    if keys[K_LEFT]:
        for block in floating_blocks:
            block.move_ip(SCROLL_SPEED, 0)
        if player_pos[0] <= LEFT_SCROLL_THRESHOLD:
            global_position -= SCROLL_SPEED
            end_flag.move_ip(SCROLL_SPEED, 0)
            for segment in terrain:
                segment.move_ip(SCROLL_SPEED, 0)

            # Prevent repopulating terrain past the beginning
            if terrain[0].left > 0 and global_position > 0:
                new_left_terrain_height = generate_terrain_height()
                new_left_segment = pygame.Rect(terrain[0].left - TERRAIN_WIDTH, new_left_terrain_height, TERRAIN_WIDTH,
                                               HEIGHT - new_left_terrain_height)
                terrain.insert(0, new_left_segment)

        else:  # Allow the player to move left within the screen, without scrolling.
            player_pos[0] -= PLAYER_SPEED

    if keys[K_UP] and on_ground:
        vy = JUMP_STRENGTH

    vy += GRAVITY
    player_pos[1] += vy

    # Check collision with terrain segments
    on_ground = False
    for segment in terrain:
        if player_pos[0] < segment.right and player_pos[0] + player_size[0] > segment.left:
            if player_pos[1] + player_size[1] > segment.top and player_pos[1] < segment.bottom:
                player_pos[1] = segment.top - player_size[1]
                vy = 0
                on_ground = True
                break

    if player_pos[1] > 700:
        reset_player()

    # Check collision with floating blocks
    for block in floating_blocks:
        if player_pos[0] < block.right and player_pos[0] + player_size[0] > block.left:
            if player_pos[1] + player_size[1] > block.top and player_pos[1] < block.bottom:
                player_pos[1] = block.top - player_size[1]
                vy = 0
                on_ground = True
                break

    for segment in terrain:
        pygame.draw.rect(screen, colors.SIENNA, segment)

    # Check for collision with the end flag
    player_rect = pygame.Rect(player_pos[0], player_pos[1], *player_size)
    if player_rect.colliderect(end_flag):
        print("Level Complete!")
        # Here, you can display a message, pause the game, or transition to another screen.
        running = False

    # Draw floating blocks
    for block in floating_blocks:
        pygame.draw.rect(screen, floating_blocks_color, block)

    # Draw the end flag
    pygame.draw.rect(screen, colors.WHITE, end_flag)

    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], *player_size))
    # screen.blit(player_images[current_frame], player_pos)
    # screen.blit(player_images[current_image_index], player_pos)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()