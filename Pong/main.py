import random
import time

from paddle import Paddle
from scoreboard import Scoreboard
from settings import setup_screen, Button, display_welcome_message, ResetButton
from ball import Ball

SELECTED_DIFFICULTY = None
BUTTONS = []


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

    def __init__(self, player_one_name, player_two_name, mode, difficulty=None):
        self.screen = setup_screen()
        self.mode = mode
        self.window_closed = False
        self.difficulty = difficulty
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.r_paddle = Paddle((350, 0))
        self.l_paddle = Paddle((-350, 0))
        self.scoreboard = Scoreboard(player_one_name=player_one_name, player_two_name=player_two_name,
                                     difficulty=self.difficulty)
        self.ball = Ball(self.scoreboard)
        self.setup_keybindings()
        self.scoreboard.display_keybindings(self.mode)
        self.r_paddle_move = 0
        self.l_paddle_move = 0
        self.game_running = True
        self.reset_button = ResetButton(self.reset_game)
        self.screen.onscreenclick(self.reset_button.on_click)
        self.screen.update()

        if self.mode == "c":
            self.scoreboard.display_difficulty(self.difficulty)

    def reset_game(self):
        self.screen.clear()
        self.ball.hideturtle()
        self.l_paddle.hideturtle()
        self.r_paddle.hideturtle()
        self.scoreboard.clear()
        game_setup(self.mode, self.player_one_name, self.player_two_name)

    def set_r_paddle_move(self, distance):
        self.r_paddle_move = distance

    def set_l_paddle_move(self, distance):
        self.l_paddle_move = distance

    def setup_keybindings(self):
        self.screen.listen()

        # One-time move on single click
        self.screen.onkey(self.l_paddle.go_up, "Up")
        self.screen.onkey(self.l_paddle.go_down, "Down")
        self.screen.onkey(self.r_paddle.go_up, "w")
        self.screen.onkey(self.r_paddle.go_down, "s")

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
            if not self.screen._root:
                self.game_running = False
            time.sleep(self.ball.ball_move_speed)
            self.screen.update()
            self.ball.move()

            if self.mode == "c":
                self.move_l_paddle_automatically()
            else:
                self.l_paddle.move_by(self.l_paddle_move)

            self.r_paddle.move_by(self.r_paddle_move)
            self.check_wall_collision()
            self.check_paddle_collision()
            self.check_r_paddle_misses()
            self.check_l_paddle_misses()

    def check_wall_collision(self):
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.bounce_y()

    def check_paddle_collision(self):
        # Detect collision with right paddle
        if self.PADDLE_RIGHT_COLLISION_MIN < self.ball.xcor() < self.PADDLE_RIGHT_COLLISION_MAX and \
                self.r_paddle.ycor() + 50 > self.ball.ycor() > self.r_paddle.ycor() - 50:
            self.ball_bounce_paddle_collision(self.r_paddle)

        # Detect collision with left paddle
        if self.PADDLE_LEFT_COLLISION_MIN < self.ball.xcor() < self.PADDLE_LEFT_COLLISION_MAX and \
                self.l_paddle.ycor() + 50 > self.ball.ycor() > self.l_paddle.ycor() - 50:
            self.ball_bounce_paddle_collision(self.l_paddle)

    def ball_bounce_paddle_collision(self, paddle):
        if paddle.ycor() + 50 > self.ball.ycor() > paddle.ycor() + 30:
            self.ball.bounce_x()
            self.ball.y_move = abs(self.ball.y_move)
        elif paddle.ycor() - 50 < self.ball.ycor() < paddle.ycor() - 30:
            self.ball.bounce_x()
            self.ball.y_move = -abs(self.ball.y_move)
        else:
            self.ball.bounce_x()

    def check_r_paddle_misses(self):
        if self.ball.xcor() > self.BALL_RIGHT_BOUNDARY:
            self.scoreboard.l_point()
            if self.scoreboard.l_score >= self.POINTS_TO_WIN:
                self.end_game(self.scoreboard.player_one_name)
                return
            time.sleep(2)
            self.ball.reset_position()
            self.r_paddle.reset_position()
            self.l_paddle.reset_position()
            self.screen.update()
            self.countdown_timer(3)

    def check_l_paddle_misses(self):
        if self.ball.xcor() < self.BALL_LEFT_BOUNDARY:
            self.scoreboard.r_point()
            if self.scoreboard.r_score >= self.POINTS_TO_WIN:
                self.end_game(self.scoreboard.player_two_name)
                return
            time.sleep(2)
            self.ball.reset_position()
            self.r_paddle.reset_position()
            self.l_paddle.reset_position()
            self.screen.update()
            self.countdown_timer(3)

    def move_l_paddle_automatically(self):
        if self.difficulty == "easy":
            threshold = 0.6
        elif self.difficulty == "medium":
            threshold = 0.7
        else:  # hard
            threshold = 0.8

        move_decision = random.random() < threshold
        if move_decision:
            if self.ball.ycor() > self.l_paddle.ycor():
                self.l_paddle.go_up()
            else:
                self.l_paddle.go_down()
        else:
            if self.ball.ycor() < self.l_paddle.ycor():
                self.l_paddle.go_up()
            else:
                self.l_paddle.go_down()

    def countdown_timer(self, duration):
        for i in range(duration, 0, -1):
            self.scoreboard.display_countdown(i)
            time.sleep(1)
        self.scoreboard.clear_countdown()

    def end(self):
        def on_window_close(x, y):
            self.window_closed = True
            self.screen.bye()

        self.screen.onclick(on_window_close)

    def end_game(self, winner_name):
        self.game_running = False
        self.scoreboard.display_winner(winner_name)

        end_time = time.time() + 60
        while time.time() < end_time:
            self.screen.update()
            if self.reset_button.clicked:
                return
            time.sleep(0.1)
        self.screen.bye()


def choose_difficulty(difficulty, screen, welcome_message, difficulty_message, player_one_name, player_two_name):
    global SELECTED_DIFFICULTY, BUTTONS
    SELECTED_DIFFICULTY = difficulty

    for button in BUTTONS:
        button.hide_and_clear()

    welcome_message.clear()
    difficulty_message.clear()
    screen.update()
    screen.onscreenclick(None)

    start_game('c', player_one_name, player_two_name, difficulty)


def start_game(mode, player_one_name, player_two_name, difficulty=None):
    if mode == 'c' and not difficulty:
        raise ValueError("Must provide difficulty for computer mode.")
    game = Game(player_one_name, player_two_name, mode, difficulty)
    game.play()
    game.end()
    return game


def select_mode():
    mode = input("Play against (C)omputer or (P)layer? ").lower()
    while mode not in ["c", "p"]:
        print("Invalid choice! Please enter c to play against computer or p to play against another player.")
        mode = input("Play against (C)omputer or (P)layer? ").lower()

    player_two_name = input("Enter name for the first player: ")
    player_one_name = "Computer" if mode == "c" else input("Enter name for the second player: ")

    return mode, player_one_name, player_two_name


def game_setup(mode, player_one_name, player_two_name):
    screen = setup_screen()
    welcome_message = display_welcome_message(0, 350, "Welcome to Pong!", font_size=24)
    difficulty_message = display_welcome_message(0, 100, "Please select a difficulty:")

    if mode == "c":
        global BUTTONS
        BUTTONS = [
            Button(0, 50, "Easy (60% success)", 180, 30,
                   lambda x=None, y=None: choose_difficulty("easy", screen, welcome_message, difficulty_message,
                                                            player_one_name, player_two_name)),
            Button(0, 0, "Medium (70% success)", 180, 30,
                   lambda x=None, y=None: choose_difficulty("medium", screen, welcome_message, difficulty_message,
                                                            player_one_name, player_two_name)),
            Button(0, -50, "Hard (80% success)", 180, 30,
                   lambda x=None, y=None: choose_difficulty("hard", screen, welcome_message, difficulty_message,
                                                            player_one_name, player_two_name))
        ]

        def on_screen_click(x, y):
            for button in BUTTONS:
                if button.is_inside(x, y):
                    button.on_click(x, y)

        screen.onscreenclick(on_screen_click)
        screen.mainloop()

    else:
        welcome_message.clear()
        difficulty_message.clear()
        game = start_game(mode, player_one_name, player_two_name)
        return game


def main():
    mode, player_one_name, player_two_name = select_mode()
    while True:
        game_instance = game_setup(mode, player_one_name, player_two_name)
        if game_instance.window_closed:
            break


if __name__ == "__main__":
    main()
