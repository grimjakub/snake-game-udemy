from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write("Score: " + str(self.score), align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)