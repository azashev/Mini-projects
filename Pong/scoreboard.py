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

        self.update_score()

    def update_score(self):
        self.goto(0, 230)
        self.clear()
        self.write("The first player to reach 10 points wins!\n", align="center",
                   font=("Courier", 20, "normal"))
        self.goto(0, 210)
        self.write(f"{self.player_one_name}: {self.l_score}  {self.player_two_name}: {self.r_score}", align="center",
                   font=("Courier", 22, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def display_countdown(self, count):
        self.countdown_turtle.clear()
        self.countdown_turtle.write(str(count), align="center", font=("Courier", 48, "normal"))

    def clear_countdown(self):
        self.countdown_turtle.clear()
