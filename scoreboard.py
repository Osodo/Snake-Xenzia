from turtle import Turtle


FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.current_score = 0
        self.write_score()


    def write_score(self):
        self.clear()
        self.goto(x=-20, y= 280)
        self.write(f"Score: {self.current_score} High Score: {self.high_score}",
                    align= ALIGNMENT, font=FONT)

    def update_score(self):
        self.current_score += 1
        self.clear()
        self.write_score()
        print(self.current_score)

    def reset_score(self):
        if self.current_score > self.high_score:
            with open("data.txt", mode="w") as file:
                stringed_score = str(self.current_score)
                self.high_score = self.current_score
                file.write(stringed_score)

        self.current_score = 0
        self.write_score()
