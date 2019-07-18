import pygame as pgame
import random

class Snake:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = 0
        self.y = 0
        self.velocity = 10
        self.color = (255, 0, 0)

class Food:
    def __init__(self, x, y, color):
        self.width = 10
        self.height = 10
        self.x = x
        self.y = y
        self.color = color

class Application(object):

    def __init__(self):
        self.is_running = True
        self.snake = Snake()
        self.food = Food(300, 300, self.generate_color())
        self.window_width = 600
        self.window_height =600
        self.window = pgame.display.set_mode((self.window_height,
                                  self.window_width))


    def start_game_loop(self):
        while self.is_running:
            self.on_loop()
            pgame.display.update()
            pgame.time.delay(60)


    def generate_color(self):
        return (random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255))


    def draw_food(self):
        pgame.draw.rect(self.window, self.food.color,
                        (self.food.x, self.food.y, self.food.width, self.food.height))

    def draw_snake(self):
        pgame.draw.rect(self.window, self.snake.color,
                        (self.snake.x, self.snake.y, self.snake.width, self.snake.height))


    def generate_random_coords(self, object_width, object_height):
        x = random.randint(0, self.window_width // object_width - 1)
        y = random.randint(0, self.window_height // object_height - 1)
        return x * object_width, y * object_height


    def spawn_food(self):
        food_coords = self.generate_random_coords(self.food.width, self.food.height)
        return Food(food_coords[0], food_coords[1], self.generate_color())  # the two values, an x-coordinate and a y-coordinate

    def check_food_touched(self):
        return (self.food.x == self.snake.x and self.food.y == self.snake.y)


    def on_loop(self):
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
            if (self.snake.x- self.snake.velocity >= 0):
                self.snake.x -= self.snake.velocity
        if keys[pgame.K_RIGHT]:
            if (self.snake.x+self.snake.velocity< self.window_width):
                self.snake.x += self.snake.velocity
        if keys[pgame.K_UP]:
            if (self.snake.y-self.snake.velocity >= 0):
                self.snake.y -= self.snake.velocity
        if keys[pgame.K_DOWN]:
            if (self.snake.y+self.snake.velocity < self.window_height):
                self.snake.y += self.snake.velocity

        # the 'c' key -> generate a new color at random
        if keys[pgame.K_c]:
            # Generate a random color by drawing 3 random integers between 0 and 255.
            # One for each color channel represented by a triple (R,G,B)
            self.snake.color = self.generate_color()

        # the 'q' key --> end the game loop
        if keys[pgame.K_q]:
            self.is_running = False

        # Fill the background after moving
        self.window.fill((0, 0, 0))

        # rect(Surface, color, Rect, width=0)
        self.draw_food()
        self.draw_snake()

        if self.check_food_touched():
            self.food = self.spawn_food()


if __name__ == "__main__":
    application = Application()
    application.start_game_loop()