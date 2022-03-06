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
screen.onkey(player.move_up, '8')

count = 0
speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    if player.ycor() > 280:
        player.sety(-280)
        scoreboard.add_level()
        speed -= 0.005
        print(f'current speed is {speed} ')
    if speed <= 0.05:
        speed == 0.05
    count += 1
    if count % 10 == 0:
        car_manager.add_car()

    for i in car_manager.cars:
        i.backward(10)
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
