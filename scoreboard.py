from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def end_game(self):
        self.goto(0, 0)
        self.write(f"Game Over.", align="center", font=FONT)



