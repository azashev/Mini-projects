import random
import time

from paddle import Paddle
from scoreboard import Scoreboard
from settings import setup_screen
from ball import Ball


class Game:
    BALL_RIGHT_BOUNDARY = 380
    BALL_LEFT_BOUNDARY = -380
    BALL_UPPER_BOUNDARY = 280
    BALL_LOWER_BOUNDARY = -280

    PADDLE_RIGHT_COLLISION_MIN = 330
    PADDLE_RIGHT_COLLISION_MAX = 340
    PADDLE_LEFT_COLLISION_MIN = -340
    PADDLE_LEFT_COLLISION_MAX = -330

    POINTS_TO_WIN = 10

    def __init__(self, player_one_name, player_two_name, mode):
        self.screen = setup_screen()
        self.mode = mode
        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))
        self.ball = Ball()
        self.setup_keybindings()
        self.scoreboard = Scoreboard(player_one_name=player_one_name, player_two_name=player_two_name)
        self.r_paddle_move = 0
        self.l_paddle_move = 0
        self.game_running = True

    def set_r_paddle_move(self, distance):
        self.r_paddle_move = distance

    def set_l_paddle_move(self, distance):
        self.l_paddle_move = distance

    def setup_keybindings(self):
        self.screen.listen()

        # One-time move on single click
        self.screen.onkey(self.r_paddle.go_up, "Up")
        self.screen.onkey(self.r_paddle.go_down, "Down")
        self.screen.onkey(self.l_paddle.go_up, "w")
        self.screen.onkey(self.l_paddle.go_down, "s")

        # Continuous move on holding the key
        self.screen.onkeypress(self.start_r_paddle_up, "Up")
        self.screen.onkeyrelease(self.stop_r_paddle_move, "Up")

        self.screen.onkeypress(self.start_r_paddle_down, "Down")
        self.screen.onkeyrelease(self.stop_r_paddle_move, "Down")

        self.screen.onkeypress(self.start_l_paddle_up, "w")
        self.screen.onkeyrelease(self.stop_l_paddle_move, "w")

        self.screen.onkeypress(self.start_l_paddle_down, "s")
        self.screen.onkeyrelease(self.stop_l_paddle_move, "s")

    def start_r_paddle_up(self):
        self.set_r_paddle_move(Paddle.MOVE_DISTANCE)

    def start_r_paddle_down(self):
        self.set_r_paddle_move(-Paddle.MOVE_DISTANCE)

    def start_l_paddle_up(self):
        self.set_l_paddle_move(Paddle.MOVE_DISTANCE)

    def start_l_paddle_down(self):
        self.set_l_paddle_move(-Paddle.MOVE_DISTANCE)

    def stop_r_paddle_move(self):
        self.set_r_paddle_move(0)

    def stop_l_paddle_move(self):
        self.set_l_paddle_move(0)

    def play(self):
        self.countdown_timer(5)
        while self.game_running:
            time.sleep(self.ball.ball_move_speed)
            self.screen.update()
            self.ball.move()

            if self.mode == "c":
                self.move_r_paddle_automatically()
            else:
                self.r_paddle.move_by(self.r_paddle_move)

            self.l_paddle.move_by(self.l_paddle_move)
            self.check_wall_collision()
            self.check_paddle_collision()
            self.check_r_paddle_misses()
            self.check_l_paddle_misses()

    def check_wall_collision(self):
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.bounce_y()

    def check_paddle_collision(self):
        # Detect collision with right paddle
        if 340 > self.ball.xcor() > 330:
            if self.r_paddle.ycor() + 50 > self.ball.ycor() > self.r_paddle.ycor() + 30:
                self.ball.bounce_x()
                self.ball.y_move = abs(self.ball.y_move)
            elif self.r_paddle.ycor() - 50 < self.ball.ycor() < self.r_paddle.ycor() - 30:
                self.ball.bounce_x()
                self.ball.y_move = -abs(self.ball.y_move)
            elif self.r_paddle.ycor() + 30 > self.ball.ycor() > self.r_paddle.ycor() - 30:
                self.ball.bounce_x()

        # Detect collision with left paddle
        if -340 < self.ball.xcor() < -330:
            if self.l_paddle.ycor() + 50 > self.ball.ycor() > self.l_paddle.ycor() + 30:
                self.ball.bounce_x()
                self.ball.y_move = abs(self.ball.y_move)
            elif self.l_paddle.ycor() - 50 < self.ball.ycor() < self.l_paddle.ycor() - 30:
                self.ball.bounce_x()
                self.ball.y_move = -abs(self.ball.y_move)
            elif self.l_paddle.ycor() + 30 > self.ball.ycor() > self.l_paddle.ycor() - 30:
                self.ball.bounce_x()

    def check_r_paddle_misses(self):
        if self.ball.xcor() > self.BALL_RIGHT_BOUNDARY:
            time.sleep(2)
            self.countdown_timer(3)
            self.scoreboard.l_point()
            if self.scoreboard.l_score >= self.POINTS_TO_WIN:
                self.end_game(self.scoreboard.player_one_name)
            self.ball.reset_position()
            self.r_paddle.reset_position()
            self.l_paddle.reset_position()

    def check_l_paddle_misses(self):
        if self.ball.xcor() < self.BALL_LEFT_BOUNDARY:
            time.sleep(2)
            self.countdown_timer(3)
            self.scoreboard.r_point()
            if self.scoreboard.r_score >= self.POINTS_TO_WIN:
                self.end_game(self.scoreboard.player_two_name)
            self.ball.reset_position()
            self.r_paddle.reset_position()
            self.l_paddle.reset_position()

    def move_r_paddle_automatically(self):
        if random.choice([True, False, True, True]):
            if self.ball.ycor() > self.r_paddle.ycor():
                self.r_paddle.go_up()
            else:
                self.r_paddle.go_down()
        else:
            if self.ball.ycor() < self.r_paddle.ycor():
                self.r_paddle.go_up()
            else:
                self.r_paddle.go_down()

    def countdown_timer(self, duration):
        for i in range(duration, 0, -1):
            self.scoreboard.display_countdown(i)
            time.sleep(1)
        self.scoreboard.clear_countdown()

    def end(self):
        self.screen.exitonclick()

    def end_game(self, winner_name):
        self.game_running = False
        self.scoreboard.clear()
        self.scoreboard.write(f"{winner_name} Wins!", align="center", font=("Courier", 24, "normal"))


def main():
    mode = input("Play against (C)omputer or (P)layer? ").lower()
    while mode not in ["c", "p"]:
        print("Invalid choice! Please enter c or p to play again computer or another player.")
        mode = input("Play against (C)omputer or (P)layer? ").lower()
    player_one_name = input("Enter name for player one: ")
    player_two_name = "Computer" if mode == "c" else input("Enter name for player two: ")

    game = Game(player_one_name, player_two_name, mode)
    game.play()
    game.end()


if __name__ == "__main__":
    main()
