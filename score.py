from turtle import Turtle

FONT = ('Arial', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        with open("High_Score.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.point()

    def point(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align="Center", font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_Score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.point()
