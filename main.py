from game_loop import Game, initialize_game


def main():
    screen = initialize_game()  # Set up pygame
    game = Game(screen)
    game.game_loop()


if __name__ == "__main__":
    main()
