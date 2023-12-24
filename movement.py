from pygame.locals import *
from terrain import *
from constants import *


def handle_movement(player_pos, player_rect, global_position, terrain, vy, end_flag, floating_blocks, cactus, coin_box,
                    gold_coin, on_ground, player_size, events):
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

                # Scroll floating blocks, cacti, coins, and coin bins
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

    # Check if the player is on the ground and the jump key is pressed
    if keys[K_UP] and on_ground:
        vy = -JUMP_STRENGTH

    vy += GRAVITY
    player_pos[1] += vy
    player_rect.topleft = player_pos

    return player_pos, player_rect, global_position, vy, on_ground
