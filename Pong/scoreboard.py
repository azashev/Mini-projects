from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, player_one_name, player_two_name):
        super().__init__()
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)

        self.countdown_turtle = Turtle()
        self.countdown_turtle.color("white")
        self.countdown_turtle.penup()
        self.countdown_turtle.hideturtle()
        self.countdown_turtle.goto(0, 0)

        self.keybindings_turtle = Turtle()
        self.keybindings_turtle.color("white")
        self.keybindings_turtle.penup()
        self.keybindings_turtle.hideturtle()

        self.update_score()
        self.display_keybindings()

    def update_score(self):
        self.goto(0, 230)
        self.clear()
        self.write("The first player to reach 10 points wins!\n", align="center",
                   font=("Courier", 18, "normal"))
        self.goto(0, 210)
        self.write(f"{self.player_one_name}: {self.l_score}  {self.player_two_name}: {self.r_score}", align="center",
                   font=("Courier", 20, "normal"))

    def update_ball_speed(self, speed_counter):
        self.update_score()
        self.goto(-70, 180)
        self.write(f"Ball Speed Level: {speed_counter}", align="left", font=("Courier", 10, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def display_keybindings(self, mode="c"):
        self.goto(250, 150)
        self.write(f"Controls:\nUP: ↑\nDOWN: ↓", align="left", font=("Courier", 8, "normal"))

        if mode == "p":
            self.goto(-350, 150)
            self.write(f"Controls:\nUP: W\nDOWN: S", align="left", font=("Courier", 8, "normal"))

    def display_countdown(self, count):
        self.countdown_turtle.clear()
        self.countdown_turtle.goto(0, 80)
        self.countdown_turtle.write(str(count), align="center", font=("Courier", 48, "normal"))

    def clear_countdown(self):
        self.countdown_turtle.clear()
