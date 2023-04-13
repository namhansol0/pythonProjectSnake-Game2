from turtle import Turtle
import random

class Food(Turtle): #Turtle 클래스의 기능을 사용 할 수 있음

    def __init__(self):
        super().__init__() #상위 클래스 설정
        self.shape("circle") #공 모양 설정
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #공의 크기 0.5로 설정
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)  # 범위에 랜덤하게 생성
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # 설정한 범위로 이동









