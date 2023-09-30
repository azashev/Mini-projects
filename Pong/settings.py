from turtle import Screen
from turtle import Turtle


# Screen settings
def setup_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)
    return screen


def display_welcome_message(x, y, message, font_size=18):
    message_turtle = Turtle()
    message_turtle.hideturtle()
    message_turtle.speed(0)
    message_turtle.color("white")
    message_turtle.penup()
    message_turtle.goto(x, y)
    message_turtle.write(message, align="center", font=("Courier", font_size, "normal"))
    return message_turtle


class Button(Turtle):
    def __init__(self, x, y, text, width, height, callback):
        super().__init__()

        self.callback = callback
        self.width = width
        self.height = height

        self.speed(0)
        self.penup()

        self.shape("square")
        self.shapesize(stretch_wid=height / 20, stretch_len=width / 20)
        self.color("white")
        self.goto(x, y)
        self.stamp_id = self.stamp()
        self.hideturtle()

        # New turtle instance for text
        self.text_turtle = Turtle()
        self.text_turtle.hideturtle()  # hide this turtle as well
        self.text_turtle.speed(0)
        self.text_turtle.color("black")
        self.text_turtle.penup()
        self.text_turtle.goto(x+1, y-7)
        self.text_turtle.write(text, align="center", font=("Courier", 12, "normal"))

        self.onclick(self.on_click)

    def on_click(self, x, y):
        print("Button clicked!")
        self.callback()
        self.clearstamp(self.stamp_id)
        self.clear()

    def is_inside(self, x, y):
        return (self.xcor() - self.width / 2) < x < (self.xcor() + self.width / 2) and \
            (self.ycor() - self.height / 2) < y < (self.ycor() + self.height / 2)

    def hide_and_clear(self):
        self.text_turtle.clear()  # clear the text from the text turtle
        self.clearstamp(self.stamp_id)  # Clears the white square
        self.clear()

