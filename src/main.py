import pygame


from identify_event import identify_event
from handle_click import handle_click
from draw_board import draw_board
from specs import TILE_SIZE


def main():
    WIDTH, HEIGHT = (TILE_SIZE * 10), (TILE_SIZE * 10)
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess Engine')
    clock = pygame.time.Clock()
    run = True

    # Initial board
    board = (
        ('w', False, 2, 'r'),('b', False, 2, 'k'),('w', False, 2, 'b'),('b', False, 2, 'q'),('w', False, 2, 'K'),('b', False, 2, 'b'),('w', False, 2, 'k'),('b', False, 2, 'r'),
        ('b', False, 2, 'p'),('w', False, 2, 'p'),('b', False, 2, 'p'),('w', False, 2, 'p'),('b', False, 2, 'p'),('w', False, 2, 'p'),('b', False, 2, 'p'),('w', False, 2, 'p'),
        ('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),
        ('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),
        ('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),
        ('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),('b', False, 0, ''),('w', False, 0, ''),
        ('w', False, 1, 'p'),('b', False, 1, 'p'),('w', False, 1, 'p'),('b', False, 1, 'p'),('w', False, 1, 'p'),('b', False, 1, 'p'),('w', False, 1, 'p'),('b', False, 1, 'p'),
        ('b', False, 1, 'r'),('w', False, 1, 'k'),('b', False, 1, 'b'),('w', False, 1, 'q'),('b', False, 1, 'K'),('w', False, 1, 'b'),('b', False, 1, 'k'),('w', False, 1, 'k'),
    )

    # Switch this data structure to numbers, which can be operated on using bitwise operators
    # 0 -> tile color
    # 0 -> selected?
    # 0 -> occupant             [Left to right is top to bottom]
    # 0                         [ should be smaller and faster ]
    # 0 -> piece
    # 0
    # 0

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