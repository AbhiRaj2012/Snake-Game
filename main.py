import turtle
import time
import snake
import food
import scoreboard
import wall


screen = turtle.Screen()
screen.bgcolor("GreenYellow")
screen.title("My Snake Game")
screen.setup(700,700)
screen.tracer(0)

boundary = wall.Boundary()
snake = snake.Snake()
food = food.Food()
score_board = scoreboard.ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

run = True
while run:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increment_score()

    # detecting the collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.reset_game()
        snake.reset_snake()

    # detecting the collision with Tail
    for segment in snake.all_turtles[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset_game()
            snake.reset_snake()



screen.exitonclick()
