import pygame as pgame
import random

class Box:
    def __init__(self, x, y, color=(255, 0, 0)):
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
        self.just_ate = False

    def draw(self, window):
        for box in self.body:
            box.draw(window)


    def prepare_growth(self):
        self.just_ate = True


    def grow(self, x, y):
        self.body.append(Box(x, y))

    def drag_tail(self, pred_x, pred_y):
        for i in range(1, len(self.body)):
            curr_pos_x = self.body[i].x
            curr_pos_y = self.body[i].y
            self.body[i].x = pred_x
            self.body[i].y = pred_y
            pred_x = curr_pos_x
            pred_y = curr_pos_y
            if i == len(self.body)-1 and self.just_ate:
                self.grow(curr_pos_x, curr_pos_y)
                self.just_ate = False


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

    def check_self_collision(self):
        head_box = self.body[0]
        for i in range(1, len(self.body)):
            body_box = self.body[i]
            if head_box.x == body_box.x and head_box.y == body_box.y:
                return True
        return False

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
        self.obstacles = []
        self.window_width = 600
        self.window_height = 600
        self.window = pgame.display.set_mode((self.window_height,
                                  self.window_width))
        self.general_box_size = 10
        self.last_pressed_key = pgame.K_RIGHT


    def start_game_loop(self):
        while self.is_running:
            self.on_loop()
            pgame.display.update()
            pgame.time.delay(20)


    def generate_color(self):
        return (random.randint(100, 255),
                random.randint(100, 255),
                random.randint(100, 255))


    def draw_food(self):
        self.food.body.draw(self.window)

    def draw_snake(self):
        self.snake.draw(self.window)

    def draw_obstacles(self):
        for obs in self.obstacles:
            obs.draw(self.window)


    def generate_random_coords(self, object_width, object_height):
        x = random.randint(0, self.window_width // object_width - 1)
        y = random.randint(0, self.window_height // object_height - 1)
        return x * object_width, y * object_height


    def spawn_food(self):
        food_coords = self.generate_random_coords(self.food.body.width, self.food.body.height)
        return Food(food_coords[0], food_coords[1], self.generate_color())  # the two values, an x-coordinate and a y-coordinate

    def check_food_touched(self):
        return (self.food.body.x == self.snake.body.x and self.food.body.y == self.snake.body.y)

    def add_obstacle(self):
        coords = self.generate_random_coords(self.general_box_size, self.general_box_size)
        self.obstacles.append(Box(coords[0], coords[1]))


    def on_loop(self):
        # Handle general game 'events' - e.g. QUIT which resembles the user closing the window
        for event in pgame.event.get():
            if event.type == pgame.QUIT:
                self.is_running = False

        # get an array representing the 'pressed' state of all keys
        # is 1 at a specific index if the corresponding key is pressed, else 0
        keys = pgame.key.get_pressed()
        # this array can be used to check if specific keys are pressed

        # the four arrow keys for directed movement
        if keys[pgame.K_LEFT] and not self.last_pressed_key == pgame.K_RIGHT:
            self.last_pressed_key = pgame.K_LEFT
        if keys[pgame.K_RIGHT] and not self.last_pressed_key == pgame.K_LEFT:
            self.last_pressed_key = pgame.K_RIGHT
        if keys[pgame.K_UP] and not self.last_pressed_key == pgame.K_DOWN:
            self.last_pressed_key = pgame.K_UP
        if keys[pgame.K_DOWN] and not self.last_pressed_key == pgame.K_UP:
            self.last_pressed_key = pgame.K_DOWN

        if self.last_pressed_key == pgame.K_LEFT:
            self.snake.move_left()
        if self.last_pressed_key == pgame.K_RIGHT:
            self.snake.move_right()
        if self.last_pressed_key == pgame.K_DOWN:
            self.snake.move_down()
        if self.last_pressed_key == pgame.K_UP:
            self.snake.move_up()

        snakehead = self.snake.body[0]
        if snakehead.x < 0:
            snakehead.x = self.window_width - self.general_box_size
        if snakehead.x >= self.window_width:
            snakehead.x = 0
        if snakehead.y < 0:
            snakehead.y = self.window_height - self.general_box_size
        if snakehead.y >= self.window_height:
            snakehead.y = 0

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
        self.draw_obstacles()




        if self.snake.check_collision(self.food.body):
            self.snake.prepare_growth()
            self.food = self.spawn_food()
            self.add_obstacle()

        for obs in self.obstacles:
            if self.snake.check_collision(obs):
                self.is_running = False

        if self.snake.check_self_collision():
            self.is_running = False

if __name__ == "__main__":
    application = Application()
    application.start_game_loop()