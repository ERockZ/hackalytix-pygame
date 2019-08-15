from Box import Box


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