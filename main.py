from turtle import Turtle, Screen
from Snek import Snek
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snek')
screen.tracer(0)

snek = Snek()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snek.up, 'Up')
screen.onkey(snek.down, 'Down')
screen.onkey(snek.left, 'Left')
screen.onkey(snek.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    # for segment in segments:
    #     segment.forward(20)
    time.sleep(0.1)

    snek.move()

    if snek.head.distance(food) < 15:
        print('meow')
        food.refresh()
        snek.extend()
        scoreboard.increase_score()

    if snek.head.xcor() > 280 or snek.head.xcor() < -280 or snek.head.ycor() > 280 or snek.head.ycor() < -280:
        scoreboard.reset()
        game_is_on = False
        scoreboard.game_over()

    for segment in snek.segments[1:]:
        if snek.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.reset()
            snek.reset()

screen.exitonclick()
