from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt","r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(str(self.high_score))
        self.score=0
        self.write_score()
