from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.setposition(-200, 200)
        self.level = 1
        self.current_level()

    def current_level(self):
        self.write(f'Level: {self.level}', False, 'center', font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.current_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', font=FONT)
