import pygame


from identify_event import identify_event
from handle_click import handle_click
from draw_board import draw_board
from initial_board_data import initial_board
from specs import TILE_SIZE


def main():
    WIDTH, HEIGHT = (TILE_SIZE * 10), (TILE_SIZE * 10)
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess Engine')
    clock = pygame.time.Clock()
    run = True

    board = initial_board
    
    while run:
        clock.tick(60)

        current_event = identify_event(pygame.event.get())

        if current_event[0] >= 0:
            # Handle click events
            board = handle_click(current_event, board)

        elif current_event[0] == -1:
            # Handle quit events
            run = False

        draw_board(WIN, board)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()