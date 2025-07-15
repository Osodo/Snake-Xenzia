from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)
speed = 0.5
snake = Snake()
food = Food()
score = Scoreboard()

snake.create_snake()
screen.listen()
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.left, key = "Left")
screen.onkey(fun = snake.right, key = "Right")

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move_snake()

# detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend_snake()
        speed * 1.1
          
# detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.reset_snake()


# detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10: 
            score.reset_score()
            snake.reset_snake()
 





screen.exitonclick()