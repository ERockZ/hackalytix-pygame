import pygame as pgame
import random

class Box:
    def __init__(self, x, y, color):
        self.width = 10
        self.height = 10
        self.x = x
        self.y = y
        self.color = color

    def draw(self, window):
        pgame.draw.rect(window, self.color,
                        (self.x, self.y, self.width, self.height))

class Snake:
    def __init__(self):
        self.body = [
            Box(70, 0, (255, 0, 0)),
            Box(60, 0, (255, 0, 0)),
            Box(50, 0, (255, 0, 0))
        ]
        self.velocity = 10

    def draw(self, window):
        for box in self.body:
            box.draw(window)

    def drag_tail(self, pred_x, pred_y):
        for i in range(1, len(self.body)):
            curr_pos_x = self.body[i].x
            curr_pos_y = self.body[i].y
            self.body[i].x = pred_x
            self.body[i].y = pred_y
            pred_x = curr_pos_x
            pred_y = curr_pos_y

    def move_left(self):
        predecessor_pos_x = self.body[0].x
        predecessor_pos_y = self.body[0].y
        self.body[0].x -= 10
        self.drag_tail(predecessor_pos_x, predecessor_pos_y)

    def move_right(self):
        predecessor_pos_x = self.body[0].x
        predecessor_pos_y = self.body[0].y
        self.body[0].x += 10
        self.drag_tail(predecessor_pos_x, predecessor_pos_y)

    def move_up(self):
        predecessor_pos_x = self.body[0].x
        predecessor_pos_y = self.body[0].y
        self.body[0].y -= 10
        self.drag_tail(predecessor_pos_x, predecessor_pos_y)

    def move_down(self):
        predecessor_pos_x = self.body[0].x
        predecessor_pos_y = self.body[0].y
        self.body[0].y += 10
        self.drag_tail(predecessor_pos_x, predecessor_pos_y)

    def check_collision(self, box):
        for el in self.body:
            if el.x == box.x and el.y == box.y:
                return True
        return False


class Food:
    def __init__(self, x, y, color):
        self.body = Box(x, y, color)


class Application(object):

    def __init__(self):
        self.is_running = True
        self.snake = Snake()
        self.food = Food(300, 300, self.generate_color())
        self.window_width = 600
        self.window_height = 600
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
        pgame.draw.rect(self.window, self.food.body.color,
                        (self.food.body.x, self.food.body.y, self.food.body.width, self.food.body.height))

    def draw_snake(self):
        self.snake.draw(self.window)


    def generate_random_coords(self, object_width, object_height):
        x = random.randint(0, self.window_width // object_width - 1)
        y = random.randint(0, self.window_height // object_height - 1)
        return x * object_width, y * object_height


    def spawn_food(self):
        food_coords = self.generate_random_coords(self.food.body.width, self.food.body.height)
        return Food(food_coords[0], food_coords[1], self.generate_color())  # the two values, an x-coordinate and a y-coordinate

    def check_food_touched(self):
        return (self.food.body.x == self.snake.body.x and self.food.body.y == self.snake.body.y)


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
        #    if (self.snake.body.x-self.snake.velocity >= 0):
            self.snake.move_left()
        if keys[pgame.K_RIGHT]:
        #    if (self.snake.body.x+self.snake.velocity< self.window_width):
            self.snake.move_right()
        if keys[pgame.K_UP]:
        #    if (self.snake.body.y-self.snake.velocity >= 0):
            self.snake.move_up()
        if keys[pgame.K_DOWN]:
        #    if (self.snake.body.y+self.snake.velocity < self.window_height):
            self.snake.move_down()

        # the 'c' key -> generate a new color at random
        #if keys[pgame.K_c]:
            # Generate a random color by drawing 3 random integers between 0 and 255.
            # One for each color channel represented by a triple (R,G,B)
        #    self.snake.color = self.generate_color()

        # the 'q' key --> end the game loop
        if keys[pgame.K_q]:
            self.is_running = False

        # Fill the background after moving
        self.window.fill((0, 0, 0))

        # rect(Surface, color, Rect, width=0)
        self.draw_food()
        self.draw_snake()

        if self.snake.check_collision(self.food.body):
            self.food = self.spawn_food()


if __name__ == "__main__":
    application = Application()
    application.start_game_loop()