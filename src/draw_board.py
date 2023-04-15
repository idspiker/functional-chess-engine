from specs import TILE_SIZE
from pick_piece import pick_piece
import images


def draw_board(window, board, x=TILE_SIZE, y=TILE_SIZE):
    if len(board) == 0:
        return
    
    window.blit(
        (images.LIGHT_TILE_IMAGE 
         if board[0].tile_color == 'w' 
         else images.DARK_TILE_IMAGE),
        (x, y)
    )

    # Draw selected
    if board[0].is_selected == True:
        window.blit(images.SELECTED_TILE_OVERLAY_IMAGE, (x, y))
    
    # Draw highlight
    if board[0].is_highlighted == True:
        window.blit(images.TILE_OVERLAY_IMAGE, (x, y))

    # If occupied, draw piece
    if board[0].occupant_team != 0:
        window.blit(pick_piece(board[0].occupant_team, board[0].piece), (x, y))

    if x == TILE_SIZE * 8:
        x = 0
        y += TILE_SIZE

    draw_board(window, board[1:], x + TILE_SIZE, y)
