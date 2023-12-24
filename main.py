from game_loop import Game
import pygame
import sys


def initialize_game(screen):
    game = Game(screen)
    game.game_loop()


def main_menu(screen):
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    menu_items = ['Play', 'Show Scores', 'Quit']
    selected_item = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if menu_items[selected_item] == 'Play':
                        initialize_game(screen)
                    elif menu_items[selected_item] == 'Show Scores':
                        # Show scores
                        pass
                    elif menu_items[selected_item] == 'Quit':
                        pygame.quit()
                        sys.exit()

        screen.fill((0, 0, 0))  # Black background

        for i, item in enumerate(menu_items):
            if i == selected_item:
                text = font.render(item, True, (255, 0, 0))  # Highlighted in red
            else:
                text = font.render(item, True, (255, 255, 255))  # White for other items
            text_rect = text.get_rect(center=(screen.get_width() / 2, 100 + 30 * i))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)


def main():
    pygame.init()
    screen = pygame.display.set_mode((1480, 900))
    main_menu(screen)


if __name__ == "__main__":
    main()
