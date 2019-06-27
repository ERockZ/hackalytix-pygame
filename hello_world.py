import pygame as pgame
import random


def run_game():

    # First some variables and subroutines for setting up the initial state of the game

    # initialize game engine, all needed modules
    pgame.init()

    window_width = 600
    window_height = 600

    # player rectangle dimensions
    width = window_width / 10
    height = window_height / 10

    playfield_margin_x = 10
    playfield_margin_y = 10

    food_coords = generate_random_coords(window_width, window_height, width, height, playfield_margin_x, playfield_margin_y)

    food = (food_coords[0], # x coordinate
            food_coords[1],# y coordinate
            width, # width
            height,# height
            generate_color()) # the two values, an x-coordinate and a y-coordinate‚

    # set the game's screen size
    win = pgame.display.set_mode((window_height + playfield_margin_y * 2,
                                  window_width + playfield_margin_x * 2))

    # set screen title
    pgame.display.set_caption("Snake Project")

    # player start coordinates

    #x, y = generate_random_coords(window_width, window_height, width, height)

    x = playfield_margin_x
    y = playfield_margin_y


    # 'velocity'
    vel_x = width
    vel_y = height

    # standard cube color
    color = (255, 0, 0)


    run = True
    # begin an endless loop in which the game state will be continuously updated
    while run:

        # Handle general game 'events' - e.g. QUIT which resembles the user closing the window
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                run = False

        # get an array representing the 'pressed' state of all keys
        # is 1 at a specific index if the corresponding key is pressed, else 0
        keys = pgame.key.get_pressed()
        # this array can be used to check if specific keys are pressed

        # the four arrow keys for directed movement
        if keys[pgame.K_LEFT]:
            if (x-vel_x >= 0):
                x -= vel_x
        if keys[pgame.K_RIGHT]:
            if (x+vel_x < window_width):
                x += vel_x
        if keys[pgame.K_UP]:
            if (y-vel_y >= 0):
                y -= vel_y
        if keys[pgame.K_DOWN]:
            if (y+vel_y < window_height):
                y += vel_y

        # the 'c' key -> generate a new color at random
        if keys[pgame.K_c]:
            # Generate a random color by drawing 3 random integers between 0 and 255.
            # One for each color channel represented by a triple (R,G,B)
            color = generate_color()

        # the 'q' key --> end the game loop
        if keys[pgame.K_q]:
            run = False

        # Fill the background after moving
        win.fill((0, 0, 0))

        # rect(Surface, color, Rect, width=0)
        draw_food(win, food)
        pgame.draw.rect(win, color, (x, y, width, height))


        food = check_food_touched(food, (x, y), window_width, window_height, width, height, playfield_margin_x, playfield_margin_x)

        # pygame module to control the display window and screen
        pgame.display.update()

        # delay time before next update --> adjust for smoother/choppier feeling
        pgame.time.delay(60)

    # quit the game, return an 'exit code' of 0
    pgame.quit()
    return 0

def check_food_touched(food, player, window_width, window_height, width, height, margin_x, margin_y):
    print(player[0], player[1])
    print(food[0], food[1])
    if (food[0] == player[0] and food[1] == player[1]):
        food_coords = generate_random_coords(window_width, window_height, width, height, margin_x, margin_y)
        food = (food_coords[0],
                food_coords[1],
                width, # width
                height,# height
                generate_color()) # the two values, an x-coordinate and a y-coordinate
    return food

def generate_random_coords(window_width, window_height, object_width, object_height, margin_x, margin_y):
    """
    will generate random coordinates which are aligned with the grid imposed onto the playfield
    :param window_width:
    :param window_height:
    :param object_width:
    :param object_height:
    :return: (x, y)
    """
    x = random.randint(0, window_width // object_width - 1)
    y = random.randint(0, window_height // object_height - 1)
    return x*object_width + margin_x, y*object_height + margin_y


def generate_color():
    return (random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255))

def draw_food(window, food):
    food_x = food[0]
    food_y = food[1]
    food_with = food[2]
    food_height = food[3]
    color = food[4]
    pgame.draw.rect(window, color, (food_x, food_y, food_with, food_height))



if __name__ == "__main__":
    run_game()