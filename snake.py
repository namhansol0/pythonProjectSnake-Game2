from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #각 블럭의 시작위치
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake() #뱀을 만든다.
        self.head = self.segments[0] #뱀의 머리

    def create_snake(self): #뱀을 만든다.
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # 방향을 바꿧을 때 좌표
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)  # 첫 번쩨 블럭이 20만큼 이동한다.

    def add_segment(self, position): #뱀이 먹이를 먹을 때마다 새로운 새그먼트를 추가한다.
        new_segment = Turtle("square")  # 사각형 모양
        new_segment.color("white")  # 색깔
        new_segment.penup()  # 선을 없앤다
        new_segment.goto(position)  # 위치
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position()) #새그먼트 마지막에 추가됨


    def up(self): #어떻게 하면 위쪽으로 이동할까?
        if self.head.heading() != DOWN: #윗쪽으로 이동중에 아랫쪽으로 불가
            self.head.setheading(UP) #머리가 회전하는 각도

    def down(self): #어떻게 하면 밑으로 이동할까?
        if self.head.heading() != UP: #밑으로 이동중에 윗쪽으로 불가
            self.head.setheading(DOWN)
    def left(self): #어떻게 하면 왼쪽으로 이동할까?
        if self.head.heading() != RIGHT: #왼쪽으로 이동중에 오른쪽으로 불가
            self.head.setheading(LEFT)
    def right(self): #어떻게 하면 오른쪽으로 이동할까?
        if self.head.heading() != LEFT: #오른쪽으로 이동중에 왼쪽으로 불가
            self.head.setheading(RIGHT)

