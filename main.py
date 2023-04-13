from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time #시간 설정

screen = Screen()
screen.setup(width=600, height=600) #화면크기
screen.bgcolor("black") #화면 색
screen.title("My Snake Game") #게임 타이틀
screen.tracer(0) #화면 잇기

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up") #윗 키
screen.onkey(snake.down, "Down") # 아랫 키
screen.onkey(snake.left, "Left") # 왼 쪽
screen.onkey(snake.right, "Right") # 오른쪽


game_is_on = True
while game_is_on: #게임이 실행하는 동안
    screen.update() #화면 업데이트
    time.sleep(0.08) #0.1초 지연시간
    snake.move()

    if snake.head.distance(food) < 15:  #뱀의 머리가 먹이의 거리보다 작다면(먹이크기 100)
        food.refresh() #먹이를 다시 생성
        snake.extend() #먹이를 먹으면 뱀의 길이도 증가
        scoreboard.increase_score()

    #벽과의 충돌 감지
    #뱀 머리의 x좌표값이 280보다 크다면 + -280보다 작다면 y좌표가 280, -280보다 크거나 작다면 충돌
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #꼬리와 충돌하면, 충돌감지하는 방법법
    for segment in snake.segments: #뱀의 모든 세그먼트를 가저옴
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10: #충돌감지
            game_is_on = False
            scoreboard.game_over()
    #머리가 꼬리의 아무 세그먼트랑 맛물리면 게임이 끝남


screen.exitonclick() #창을 클릭하면 없어짐

























