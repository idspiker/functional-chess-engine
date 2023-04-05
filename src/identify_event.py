import pygame
from typing import Tuple, List

def identify_event(events: List[pygame.event.Event]) -> Tuple[int, int]:
    if len(events) == 0:
        return (-2, -2)
    elif events[0].type == pygame.QUIT:
        return (-1, -1)
    elif events[0].type == pygame.MOUSEBUTTONDOWN:
        return events[0].pos
    
    return identify_event(events[1:])
