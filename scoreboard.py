from turtle import Turtle
ALİGNMENT = "center"
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.skor_guncelleme()

    def skor_guncelleme(self):
        self.write(f"Score: {self.score}",align=ALİGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.",align=ALİGNMENT,font=FONT)

    def skor_arttirma(self):
        self.score += 10
        self.clear()
        self.skor_guncelleme()
        