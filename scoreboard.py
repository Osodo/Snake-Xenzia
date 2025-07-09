from turtle import Turtle


FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.current_score = 0
        self.write_score()


    def write_score(self):
        self.goto(x=-20, y= 280)
        self.write(f"Score: {self.current_score}", align= ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write_score()
        print(self.current_score)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align= ALIGNMENT, font=FONT)