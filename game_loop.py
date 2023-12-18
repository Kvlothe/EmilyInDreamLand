from draw_objects import *
from movement import *


def initialize_game():
    # Initialize pygame and set up the screen
    pygame.init()
    pygame.font.init()

    # Get the size of the current screen
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

    # Set up the screen in full-screen mode
    screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
    pygame.display.set_caption("Emily in Dreamland")

    return screen


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
        self.terrain = generate_precise_terrain()
        self.floating_blocks = float_blocks()
        self.cactus = cactus_blocks()
        self.coin_box = coin_bins()
        self.gold_coin = coin_gold()

        # Initialize global_position, vertical speed (vy), and on_ground
        self.global_position = 0  # Starting global position
        self.vy = 0  # Starting vertical speed
        self.on_ground = False  # Player is initially not on the ground
        self.score = 0

        # Define end flag after the last terrain segment
        self.flag_width, self.flag_height = 10, 1150
        self.flag_pos = [self.terrain[-1]['rect'].right, self.terrain[-1]['rect'].top - self.flag_height]
        self.end_flag = pygame.Rect(self.flag_pos[0], self.flag_pos[1], self.flag_width, self.flag_height)

        self.reset_game_state()

    def reset_game_state(self):
        # Reset player position and related attributes
        self.player_pos = [0, 660]  # Example starting position
        self.player_size = (30, 40)  # Player size
        self.player_color = PINK  # Player color
        self.score = 0  # Reset score
        self.player_rect = pygame.Rect(*self.player_pos, *self.player_size)  # Create a Rect for the player

    def handle_jump(self, keys):
        if keys[K_UP] and self.on_ground:
            self.vy = -JUMP_STRENGTH
            self.on_ground = False
            print("Jump initiated, vy:", self.vy)

    def display_scoreboard(self, screen, score, elapsed_time):
        # Clear the screen or draw a background for the scoreboard
        screen.fill((0, 0, 0))  # Black background

        font = pygame.font.Font(None, 36)  # You can choose a different font or size

        # Render the final score
        score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (100, 100))  # Adjust position as needed

        prompt_text = font.render("Play Again? Y/N", True, (255, 255, 255))
        screen.blit(prompt_text, (100, 200))  # Adjust position as needed

        # Update the display
        pygame.display.flip()

    def reset_player(self):
        self.player_pos = [0, 860]
        self.vy = 0

    def game_loop(self):
        running = True
        while running:
            self.screen.fill(BLUE)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.type == KEYDOWN:
                        if event.key == K_p:
                            print("Debug Information:")
                            print(f"Global Position: {self.global_position}")
                            print(f"Player Position: {self.player_pos[0]}, {self.player_pos[1]}")
                            for i in range(5):  # Print first 5 terrain segments as an example
                                print(f"Terrain Segment {i}: {self.terrain[i]['rect']}")
                                print(f"End Flag Position: {self.end_flag}")

                            # Print information for the first few terrain segments
                            for i, segment in enumerate(self.terrain[:5]):  # Adjust the range as needed
                                print(f"Terrain Segment {i}: {segment['rect']}")

            keys = pygame.key.get_pressed()
            # self.handle_jump(keys)

            objects = self.floating_blocks + self.cactus + self.coin_box + self.gold_coin

            draw_floating_blocks(self.screen, self.floating_blocks, self.terrain, self.global_position)
            draw_cacti(self.screen, self.cactus, self.terrain, self.global_position)
            draw_gold_coin(self.screen, self.gold_coin, self.terrain, self.global_position)
            draw_coin_boxes(self.screen, self.coin_box, self.terrain, self.global_position)

            # Movement
            # Calling the handle_movement function and updating class attributes accordingly
            player_pos, player_rect, global_position, vy, on_ground = handle_movement(
                self.player_pos, self.player_rect, self.global_position, self.terrain, self.vy, self.end_flag,
                self.floating_blocks, self.cactus, self.coin_box, self.gold_coin, self.on_ground, self.player_size, events)

            # Update the class attributes with the returned values
            self.player_pos = player_pos
            self.player_rect = player_rect
            self.global_position = global_position
            self.vy = vy
            self.on_ground = on_ground

            # Check collision with terrain segments
            self.on_ground = False
            for segment_dict in self.terrain:
                segment = segment_dict['rect']  # Access the pygame.Rect object
                if player_pos[0] < segment.right and player_pos[0] + player_size[0] > segment.left:
                    if player_pos[1] + player_size[1] > segment.top and player_pos[1] < segment.bottom:
                        player_pos[1] = segment.top - player_size[1]
                        self.vy = 0
                        self.on_ground = True
                        break

            if player_pos[1] > FALL_LIMIT:
                self.reset_player()  # This resets the player to the starting position

            # Check for collision with the end flag
            if player_rect.colliderect(self.end_flag):
                final_score = self.score + (500 - int(elapsed_time))
                # Display the scoreboard
                self.display_scoreboard(self.screen, final_score, elapsed_time)

                # Pause for a moment to display the scoreboard
                pygame.time.wait(5000)  # Wait for 5 seconds, adjust as needed

                # Here, you can display a message, pause the game, or transition to another screen.
                running = False

            # Check collision with floating blocks
            for block_info in self.floating_blocks:
                # Calculate the block's rect based on its properties and the associated terrain segment
                terrain_segment = self.terrain[block_info["terrain_index"]]['rect']
                block_x = terrain_segment.x + block_info["offset_x"] - global_position
                block_y = terrain_segment.y - block_info["height_above_terrain"]
                block_rect = pygame.Rect(block_x, block_y, block_info['width'], block_info['height'])

                if player_rect.colliderect(block_rect):
                    player_pos[1] = block_rect.top - player_size[1]
                    vy = 0
                    self.on_ground = True
                    break

            # Check collision with coin bins
            for coin_info in self.coin_box:
                # Calculate the coin's rect based on its properties and the associated terrain segment
                terrain_segment = self.terrain[coin_info["terrain_index"]]['rect']
                coin_x = terrain_segment.x + coin_info["offset_x"] - global_position
                coin_y = terrain_segment.y - coin_info["height_above_terrain"]
                coin_rect = pygame.Rect(coin_x, coin_y, coin_info["width"], coin_info["height"])

                if player_rect.colliderect(coin_rect):
                    self.score += 10  # Increase score for each collected gold coin
                    self.coin_box.remove(coin_info)  # Remove the collected coin
                    break  # Exit the loop to avoid multiple coin removals in a single frame

            # Check collision with gold coins
            for gold_coin_info in self.gold_coin:
                # Calculate the coin's rect based on its properties and the associated terrain segment
                terrain_segment = self.terrain[gold_coin_info["terrain_index"]]['rect']
                coin_x = terrain_segment.x + gold_coin_info["offset_x"] - global_position
                coin_y = terrain_segment.y - gold_coin_info["height_above_terrain"]
                coin_rect = pygame.Rect(coin_x, coin_y, gold_coin_info["width"], gold_coin_info["height"])

                if player_rect.colliderect(coin_rect):
                    self.score += 10  # Increase score for each collected gold coin
                    self.gold_coin.remove(gold_coin_info)  # Remove the collected coin
                    break  # Exit the loop to avoid multiple coin removals in a single frame

            # Check collision with cactus blocks
            for cactus_info in self.cactus:
                # Calculate the cactus's rect based on its properties and the associated terrain segment
                terrain_segment = self.terrain[cactus_info["terrain_index"]]['rect']
                cactus_x = terrain_segment.x + cactus_info["offset_x"] - global_position
                cactus_y = terrain_segment.y - cactus_info["height_above_terrain"]
                cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_info["width"], cactus_info["height"])

                if player_rect.colliderect(cactus_rect):
                    self.score = max(self.score - 10, 0)  # Deduct 10 points but not below 0
                    self.reset_player()  # Reset the player if they touch the cactus
                    break  # Exit the loop to avoid multiple resets

            for segment in self.terrain:
                pygame.draw.rect(self.screen, segment['color'], segment['rect'])

            # Attempt to modulate collision checks
            # score, player_pos, vy, on_ground = handle_player_object_collisions(player_rect, objects, score, player_pos,
            #                                                                    player_size, vy, on_ground)

            # Update the timer
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - self.start_time) // 1000  # Convert milliseconds to seconds

            # Render the timer on the screen
            # You can use a pygame font object to render the elapsed time as text
            font = pygame.font.Font(None, 36)
            timer_text = font.render(str(elapsed_time), True, (255, 255, 255))
            self.screen.blit(timer_text, (10, 50))  # Position the text at the top-left corner of the screen

            # Draw the end flag
            pygame.draw.rect(self.screen, BLACK, self.end_flag)

            # Display Score
            font = pygame.font.Font(None, 36)  # Create a font object; None uses the default font, 36 is the size
            score_text = font.render(f'Score: {self.score}', True, WHITE)  # Create a text surface
            self.screen.blit(score_text, (10, 10))  # Draw the text at the top-left corner (10, 10) coordinates

            pygame.draw.rect(self.screen, self.player_color, (player_pos[0], player_pos[1], *player_size))
            pygame.display.flip()

            # play_again = False
            # waiting_for_input = True
            #
            # while waiting_for_input:
            #     for event in pygame.event.get():
            #         if event.type == pygame.KEYDOWN:
            #             if event.key == pygame.K_y:
            #                 play_again = True
            #                 waiting_for_input = False
            #             elif event.key == pygame.K_n:
            #                 play_again = False
            #                 waiting_for_input = False
            #         elif event.type == pygame.QUIT:
            #             waiting_for_input = False
            #             play_again = False
            #
            # # After the loop
            # if play_again:
            #     reset_game()
            #     continue  # Continue the game loop
            # else:
            #     # Exit the game loop to quit the game
            #     running = False

            self.clock.tick(60)

        pygame.quit()
