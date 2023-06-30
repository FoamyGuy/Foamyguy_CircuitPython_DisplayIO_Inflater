import time

import board
import displayio
from foamyguy_displayio_inflater.absolute_layout import AbsoluteLayout
from blinka_displayio_pygamedisplay import PyGameDisplay
import pygame

display = PyGameDisplay(width=500, height=300)

f = open("../layouts/button_test.json", "r")
layout_str = f.read()
f.close()
main_layout = AbsoluteLayout(display, layout_str)

display.show(main_layout.view)

button = main_layout.sub_view_by_id("main_btn").button

# Loop and look for touches
while True:
    # get mouse up  events
    ev = pygame.event.get()

    # proceed events
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(f"rel: {pos}")
            if button.selected:
                button.selected = False
            if button.contains(pos):
                print("released")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if button.contains(pos):
                button.selected = True


    if display.check_quit():
        break