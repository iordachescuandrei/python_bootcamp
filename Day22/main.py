from turtle import Screen, Turtle
from paddle import Paddle
from bapp import Ball
import time
from scoreboard import Scoreboard
screen = Screen ()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle= Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game = True
while game is True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    #detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when r_paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect when r_paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()