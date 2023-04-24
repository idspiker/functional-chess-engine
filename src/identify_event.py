import pygame
from typing import Tuple, List


from utility_funcs import is_empty


def identify_event(events: List[pygame.event.Event]) -> Tuple[int, int]:
    return (
        (-2, -2) 
        if is_empty(events)
            else tup
            if (tup := get_event_tuple(events[0]))
                else identify_event(events[1:])
    )


def get_event_tuple(event):
    return (
        (-1, -1) 
        if is_quit_event(event) 
            else event.pos 
            if is_click_event(event) 
                else tuple()
    )


def is_quit_event(event):
    return event.type == pygame.QUIT


def is_click_event(event):
    return event.type == pygame.MOUSEBUTTONDOWN
    