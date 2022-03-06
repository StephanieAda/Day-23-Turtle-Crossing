import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')

count = 0
speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    # detect successful crossing
    if player.ycor() > 280:
        player.sety(-280)
        scoreboard.add_level()
        speed -= 0.01
        print(f'current speed is {speed} ')

    if speed <= 0.005:
        speed = 0.03

    # add new cars
    count += 1
    if count % 10 == 0:
        car_manager.add_car()

    if count == 2:
        count = 6
        print(count)

    # move cars
    for i in car_manager.cars:
        i.backward(10)
        # detect collision with turtle
        # if player.distance(i) < 20:
        #     game_is_on = False
        #     scoreboard.game_over()

screen.exitonclick()
