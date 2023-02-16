from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_num = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.set_position()
        self.clear()
        self.write(f"Score: {self.score_num} High Score: {self.high_score}", True, font=FONT, align=ALIGNMENT)


    def set_position(self):
        self.goto(0, 270)

    def increase_score(self):
        self.score_num += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
        self.score_num = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
