# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color

# creating list in which we will store
# the position of the circle
pygame.draw.rect(window, (0,   0, 255),
                 [100, 100, 400, 100], 0)

rect_positions = []
# radius of the circle


# Color of the circle
color = (0, 0, 255)

# Creating a variable which we will use
# to run the while loop
run = True

# Creating a while loop
while run:
    window.fill((255, 255, 255))

    # Iterating over all the events received from
    # pygame.event.get()
    for event in pygame.event.get():

        # If the type of the event is quit
        # then setting the run variable to false
        if event.type == QUIT:
            run = False

        # if the type of the event is MOUSEBUTTONDOWN
        # then storing the current position
        elif event.type == MOUSEBUTTONDOWN:
            position = event.pos
            rect_positions.append(position)
            
    # Using for loop to iterate
    # over the circle_positions
    # list
    for position in rect_positions:

        # Drawing the circle
        pygame.draw.rect(window, color, position,)

    # Draws the surface object to the screen.
    pygame.display.update()