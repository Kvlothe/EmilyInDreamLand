import pygame
from pygame.locals import *
from colors import *
from constants import *
from terrain import *


def reset_player():
    global player_pos, vy
    player_pos = [0, 660]
    vy = 0


# Initialize pygame
pygame.init()
pygame.font.init()

# Get the size of the current screen
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
print(WIDTH)
print(HEIGHT)

# Set up the screen in full-screen mode
screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)

# Setup
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Emily in Dreamland")
clock = pygame.time.Clock()

# Start the timer
start_time = pygame.time.get_ticks()

# Gather and generate the terrain
terrain = generate_precise_terrain()
terrain = generate_precise_terrain()
print(f"Total terrain segments created: {len(terrain)}")

current_segment_index = len(terrain) - 1

# Gather Objects in level - Floating blocks, cactus and coin boxes
floating_blocks = float_blocks()
cactus = cactus_blocks()
coin_box = coin_bins()
gold_coin = coin_gold()

# Define end flag after the last terrain segment
flag_width, flag_height = 10, 1150
flag_pos = [terrain[-1]['rect'].right, terrain[-1]['rect'].top - flag_height]
# flag_pos = [terrain[99]['rect'].right, terrain[99]['rect'].top - flag_height]
end_flag = pygame.Rect(flag_pos[0], flag_pos[1], flag_width, flag_height)
# After setting the flag position
print(f"100th Terrain Segment: {terrain[99]['rect']}")
print(f"End Flag Position: {end_flag}")


# Player
# player_pos = [WIDTH / 2, HEIGHT / 2 - 50]
player_pos = [0, 860]
player_size = (30, 40)
player_color = PINK
score = 0
vy = 0  # vertical speed
on_ground = False
global_position = 50

# Create a Rect for the player
player_rect = pygame.Rect(*player_pos, *player_size)


running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    print("Debug Information:")
                    print(f"Global Position: {global_position}")
                    print(f"Player Position: {player_pos[0]}, {player_pos[1]}")
                    for i in range(5):  # Print first 5 terrain segments as an example
                        print(f"Terrain Segment {i}: {terrain[i]['rect']}")
                    print(f"End Flag Position: {end_flag}")

                    # Print information for the first few terrain segments
                    for i, segment in enumerate(terrain[:5]):  # Adjust the range as needed
                        print(f"Terrain Segment {i}: {segment['rect']}")

    keys = pygame.key.get_pressed()

    if keys[K_RIGHT]:
        can_move_right = True  # Initialize can_move_right
        # Scroll when the player reaches the scroll threshold
        if player_pos[0] >= RIGHT_SCROLL_THRESHOLD:
            if global_position + WIDTH < MAP_RIGHT_BOUNDARY:
                global_position += SCROLL_SPEED
                player_pos[0] -= SCROLL_SPEED  # Keep player position constant during scroll

                # Scroll terrain
                for segment in terrain:
                    segment.x -= SCROLL_SPEED

                # Scroll floating blocks, cacti, and coin bins
                for block_info in floating_blocks:
                    block_info["rect"].x -= SCROLL_SPEED
                for cactus_info in cactus:
                    cactus_info["rect"].x -= SCROLL_SPEED
                for coin_info in coin_box:
                    coin_info["rect"].x -= SCROLL_SPEED
                for gold_coin_info in gold_coin:
                    gold_coin_info["rect"].x -= SCROLL_SPEED

                # Update end flag position
                end_flag.x -= SCROLL_SPEED

        # Only scroll if within right boundary
        if global_position + WIDTH < MAP_RIGHT_BOUNDARY:
            # Check the height of the next terrain segment compared to the current position of the player.
            current_terrain = None
            next_terrain = None
            for i, segment in enumerate(terrain):
                if player_pos[0] + player_size[0] > segment.left and player_pos[0] < segment.right:
                    current_terrain = segment
                    if i + 1 < len(terrain):
                        next_terrain = terrain[i + 1]
                    break

            if next_terrain and current_terrain:
                potential_player_rect = pygame.Rect(player_pos[0] + PLAYER_SPEED, player_pos[1], *player_size)
                if next_terrain and potential_player_rect.colliderect(next_terrain):
                    can_move_right = False

        if player_pos[0] >= RIGHT_SCROLL_THRESHOLD:
            global_position += SCROLL_SPEED
            end_flag.x -= SCROLL_SPEED  # Move the flag left as the terrain scrolls right

            if can_move_right or not on_ground:  # Allow right movement if player is in the air
                # Scroll terrain
                for segment_info in terrain:
                    segment_info['rect'].move_ip(-SCROLL_SPEED, 0)  # Access the pygame.Rect object to move it

            elif on_ground:
                # If on ground and can't move right, push the player back slightly
                player_pos[0] -= PLAYER_SPEED

        # Otherwise, the player moves to the right as usual
        else:
            if can_move_right or not on_ground:
                player_pos[0] += PLAYER_SPEED
                player_rect.topleft = player_pos

    if keys[K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= PLAYER_SPEED
        player_rect.topleft = player_pos

        if global_position > MAP_LEFT_BOUNDARY and player_pos[0] <= LEFT_SCROLL_THRESHOLD:
            global_position -= SCROLL_SPEED
            for segment in terrain:
                segment["rect"].x += SCROLL_SPEED  # Move terrain segments rightward
            end_flag.x += SCROLL_SPEED  # Move the flag right as the terrain scrolls left

    if keys[K_UP] and on_ground:
        vy = JUMP_STRENGTH

    vy += GRAVITY
    player_pos[1] += vy
    player_rect.topleft = player_pos

    # Check collision with terrain segments
    on_ground = False
    for segment_dict in terrain:
        segment = segment_dict['rect']  # Access the pygame.Rect object
        if player_pos[0] < segment.right and player_pos[0] + player_size[0] > segment.left:
            if player_pos[1] + player_size[1] > segment.top and player_pos[1] < segment.bottom:
                player_pos[1] = segment.top - player_size[1]
                vy = 0
                on_ground = True
                break

    if player_pos[1] > FALL_LIMIT:
        reset_player()  # This resets the player to the starting position

    # Check for collision with the end flag
    if player_rect.colliderect(end_flag):
        print("Level Complete!")
        # Here, you can display a message, pause the game, or transition to another screen.
        running = False


    # Draw floating blocks
    for block_info in floating_blocks:
        terrain_segment = terrain[block_info["terrain_index"]]['rect']  # Access the pygame.Rect object
        block_x = terrain_segment.x + block_info["offset_x"] - global_position
        block_y = terrain_segment.y - block_info["height_above_terrain"]
        block_info["rect"] = pygame.Rect(block_x, block_y, block_info['width'], block_info['height'])
        # Then draw the updated block
        pygame.draw.rect(screen, floating_blocks_color, block_info["rect"])

    # Check collision with floating blocks
    for block_info in floating_blocks:
        block = block_info["rect"]
        if player_rect.colliderect(block):
            player_pos[1] = block.top - player_size[1]
            vy = 0
            on_ground = True
            break

    for coin_info in coin_box:
        terrain_segment = terrain[coin_info["terrain_index"]]['rect']
        coin_x = terrain_segment.x + coin_info["offset_x"] - global_position
        coin_y = terrain_segment.y - coin_info["height_above_terrain"]
        coin_info["rect"] = pygame.Rect(coin_x, coin_y, coin_info['width'], coin_info['height'])
        pygame.draw.rect(screen, GOLD, coin_info['rect'])

    # Check collision with coin bins
    for coin_info in coin_box:
        coin = coin_info["rect"]
        if player_rect.colliderect(coin):
            score += 100  # Increase score by 100 for each coin collected, adjust as needed
            coin_box.remove(coin_info)  # Remove the collected coin

    for gold_coin_info in gold_coin:
        terrain_segment = terrain[gold_coin_info["terrain_index"]]['rect']
        coin_x = terrain_segment.x + gold_coin_info["offset_x"] - global_position
        coin_y = terrain_segment.y - gold_coin_info["height_above_terrain"]
        gold_coin_info["rect"] = pygame.Rect(coin_x, coin_y, gold_coin_info['width'], gold_coin_info['height'])
        pygame.draw.rect(screen, GOLD, gold_coin_info['rect'])

    # Check collision with coin bins
    for gold_coin_info in gold_coin:
        coin = gold_coin_info["rect"]
        if player_rect.colliderect(coin):
            score += 10
            gold_coin.remove(gold_coin_info)  # Remove the collected coin

    # Draw Cactus
    for cactus_info in cactus:
        terrain_segment = terrain[cactus_info["terrain_index"]]['rect']
        cactus_x = terrain_segment.x + cactus_info["offset_x"] - global_position
        cactus_y = terrain_segment.y - cactus_info["height_above_terrain"]  # Assuming a fixed height above the terrain
        cactus_info["rect"] = pygame.Rect(cactus_x, cactus_y, cactus_info["width"], cactus_info["height"])
        # Then draw the updated cactus
        pygame.draw.rect(screen, GREEN, cactus_info["rect"])

    # Check collision with cactus blocks
    for cactus_info in cactus:
        cactus_rect = cactus_info["rect"]
        if player_rect.colliderect(cactus_rect):
            score = max(score - 10, 0)  # Deduct 10 points but not below 0
            reset_player()  # Reset the player if they touch the cactus
            break  # Exit the loop to avoid multiple resets

    for segment in terrain:
        pygame.draw.rect(screen, segment['color'], segment['rect'])

    # Update the timer
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) // 1000  # Convert milliseconds to seconds

    # Render the timer on the screen
    # You can use a pygame font object to render the elapsed time as text
    font = pygame.font.Font(None, 36)
    timer_text = font.render(str(elapsed_time), True, (255, 255, 255))
    screen.blit(timer_text, (10, 50))  # Position the text at the top-left corner of the screen

    # Draw the end flag
    pygame.draw.rect(screen, BLACK, end_flag)

    # Display Score
    font = pygame.font.Font(None, 36)  # Create a font object; None uses the default font, 36 is the size
    score_text = font.render(f'Score: {score}', True, WHITE)  # Create a text surface
    screen.blit(score_text, (10, 10))  # Draw the text at the top-left corner (10, 10) coordinates

    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], *player_size))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
