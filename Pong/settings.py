from turtle import Screen


# Screen settings
def setup_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)
    return screen
