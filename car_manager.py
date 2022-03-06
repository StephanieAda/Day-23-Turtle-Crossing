from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.add_car()

    def add_car(self):
        for i in range(0, 4):
            car = Turtle()
            car.shape('square')
            car.penup()
            car.shapesize(1, 2)
            car.setposition(300, random.randrange(-220, 300, 30))
            car.color(random.choice(COLORS))
            self.cars.append(car)
