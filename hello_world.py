import pygame as pgame
import random

# Initialize pgame
pgame.init()

# Initialize screen size
win = pgame.display.set_mode((600, 600))

# Set screen title
pgame.display.set_caption("Snake Project - First Trial")

x = 10
y = 10
width = 20
height = 20

# Velocity
vel = 5

# initialize run status
run = True

# standard cube color
color = (255, 0, 0)

while run:
    # Delay time to move
    pgame.time.delay(50)

    # Control the event from the keyboard or the mouse
    for event in pgame.event.get():
        if event.type == pgame.QUIT:
            run = False

    keys = pgame.key.get_pressed()
    # Control the event from the keyboard or the mouse
    if keys[pgame.K_LEFT]:
        x -= vel
    if keys[pgame.K_RIGHT]:
        x += vel
    if keys[pgame.K_UP]:
        y -= vel
    if keys[pgame.K_DOWN]:
        y += vel
    if keys[pgame.K_q]:
        pgame.quit()
    if keys[pgame.K_c]:
        # generate a random color
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))

    # Fill the background after moving
    win.fill((0, 0, 0))

    # rect(Surface, color, Rect, width=0)
    pgame.draw.rect(win, color, (x, y, width, height))

    # pygame module to control the display window and screen
    pgame.display.update()

pgame.quit()
