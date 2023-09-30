from turtle import Turtle


class Ball(Turtle):
    MAX_SPEED_BOUNCES = 15
    INITIAL_SPEED = 4.2
    MAX_SPEED = INITIAL_SPEED * (1.05 ** MAX_SPEED_BOUNCES)

    def __init__(self, scoreboard):
        super().__init__()
        self.scoreboard = scoreboard
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = self.INITIAL_SPEED
        self.y_move = self.INITIAL_SPEED
        self.ball_move_speed = 0.01
        self.distance_traveled = 0
        self.speed_counter = 0

    def move(self):
        sub_steps = 5
        x_sub_move = self.x_move / sub_steps
        y_sub_move = self.y_move / sub_steps

        for _ in range(sub_steps):
            if self.distance_traveled < 500:
                new_x = self.xcor() + (x_sub_move * 0.5)
                new_y = self.ycor() + (y_sub_move * 0.5)
            else:
                new_x = self.xcor() + x_sub_move
                new_y = self.ycor() + y_sub_move

            self.distance_traveled += abs(x_sub_move) + abs(y_sub_move)
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.speed_counter < self.MAX_SPEED_BOUNCES:
            self.x_move *= 1.05

            if abs(self.x_move) > self.MAX_SPEED:
                self.x_move = self.MAX_SPEED if self.x_move > 0 else -self.MAX_SPEED

            self.speed_counter += 1
            self.scoreboard.update_ball_speed(self.speed_counter)

    def reset_position(self):
        self.goto(0, 0)
        if self.x_move >= 0:
            self.x_move = -self.INITIAL_SPEED
        else:
            self.x_move = self.INITIAL_SPEED

        self.distance_traveled = 0
        self.speed_counter = 0
