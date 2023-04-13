from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self): #스코어보드 설정
        super().__init__()
        self.score = 0
        self.color("white") #하얀색으로 설정(중요)
        self.penup()
        self.goto(0, 270)  # 점수판을 이동
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1 #1씩 증가한다.
        self.clear() #점수판을 지우고 새로 올라간다.
        self.update_scoreboard()


