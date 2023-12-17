# Constants
WIDTH, HEIGHT = 1920, 1080
PLAYER_SPEED = 5
GRAVITY = 0.5
JUMP_STRENGTH = -15
SCROLL_SPEED = 5
TERRAIN_WIDTH = 100
LEFT_SCROLL_THRESHOLD = WIDTH * 0.25  # This means the screen starts scrolling when the player is 25% from the left edge
RIGHT_SCROLL_THRESHOLD = WIDTH * 0.75
GROUND_HEIGHT = 100

MAP_LEFT_BOUNDARY = 0
MAP_RIGHT_BOUNDARY = 100  # Adjust this based on your map size
FALL_LIMIT = 1000  # Adjust this value based on your game's needs