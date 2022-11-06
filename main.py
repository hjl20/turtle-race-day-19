from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
OFFSET = 25
start_x = -SCREEN_WIDTH / 2 + OFFSET
end_x = SCREEN_WIDTH / 2 - OFFSET
start_y = -SCREEN_HEIGHT / 6
end_y = SCREEN_WIDTH / 6


def create_racers():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for i in range(len(colors)):
        racer = Turtle(shape="turtle")
        racer.color(colors[i])
        racer.penup()
        racer.goto(start_x, start_y + i * OFFSET)


def draw_finish_line():
    finish_t = Turtle()
    finish_t.penup()
    finish_t.goto(end_x, end_y)
    finish_t.pendown()
    finish_t.goto(end_x, start_y - OFFSET)
    finish_t.penup()
    finish_t.hideturtle()


def turtle_race():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    user_bet = screen.textinput(title="Make your bet",
                                prompt="Which turtle will win the race? Enter a color: ").lower()
    
    create_racers()
    draw_finish_line()
    
    in_race = True
    while in_race:
        for t in screen.turtles():
            t.forward(random.randint(0, 4))
            if t.xcor() == end_x:
                if t.color()[0] == user_bet:
                    return "You won!"
                else:
                    return "You lost!"
    screen.exitonclick()


print(turtle_race())
