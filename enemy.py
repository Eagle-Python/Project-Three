from turtle import Turtle, Screen
import random
import time
import os
from score import Score

score = Score()


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 3  # Speed of car movement
        self.screen = Screen()
        self.screen.tracer(0)  # Turn off automatic screen updates for smoother animation
        self.f_frames = [
            "other_hero/warrior/frame_0.gif", "other_hero/warrior/frame_1.gif", "other_hero/warrior/frame_2.gif", "other_hero/warrior/frame_3.gif",
            "other_hero/warrior/frame_4.gif", "other_hero/warrior/frame_5.gif", "other_hero/warrior/frame_6.gif", "other_hero/warrior/frame_7.gif"
        ]
        self.hero_frames = [
            "other_hero/knight/frame_0.gif", "other_hero/knight/frame_1.gif", "other_hero/knight/frame_2.gif", "other_hero/knight/frame_3.gif",
            "other_hero/knight/frame_4.gif", "other_hero/knight/frame_5.gif", "other_hero/knight/frame_6.gif", "other_hero/knight/frame_7.gif"
        ]
        self.fire_frames = [
            "other_hero/snake/frame_0.gif", "other_hero/snake/frame_1.gif", "other_hero/snake/frame_2.gif", "other_hero/snake/frame_3.gif",
            "other_hero/snake/frame_4.gif", "other_hero/snake/frame_5.gif", "other_hero/snake/frame_6.gif", "other_hero/snake/frame_7.gif",
            "other_hero/snake/frame_8.gif",
        ]
        self.evil_one_frames = [
            "other_hero/evil_one/frame_0.gif", "other_hero/evil_one/frame_1.gif", "other_hero/evil_one/frame_2.gif", "other_hero/evil_one/frame_3.gif",
            "other_hero/evil_one/frame_4.gif", "other_hero/evil_one/frame_5.gif", "other_hero/evil_one/frame_6.gif", "other_hero/evil_one/frame_7.gif",
            "other_hero/evil_one/frame_8.gif", "other_hero/evil_one/frame_9.gif", "other_hero/evil_one/frame_10.gif", "other_hero/evil_one/frame_11.gif"
        ]
        self.evil_frames = [
            "other_hero/evil_two/frame_0.gif", "other_hero/evil_two/frame_1.gif", "other_hero/evil_two/frame_2.gif", "other_hero/evil_two/frame_3.gif",
            "other_hero/evil_two/frame_4.gif", "other_hero/evil_two/frame_5.gif", "other_hero/evil_two/frame_6.gif", "other_hero/evil_two/frame_7.gif"
        ]

        # Load frames as shapes
        for frames_list in [self.f_frames, self.hero_frames, self.fire_frames, self.evil_frames]:
            for frame in frames_list:
                if os.path.exists(frame):  # Ensure each frame exists
                    self.screen.addshape(frame)
                else:
                    print(f"Warning: Frame {frame} not found.")

    def create_car(self):
        # Create a new car (Turtle) with a random initial lane (y-coordinate)
        car = Turtle()
        car.penup()
        car.speed("fastest")

        # Randomly select a frame set for the car and assign it as a car attribute
        car.frames = random.choice([self.f_frames, self.hero_frames, self.fire_frames, self.evil_frames])
        car.frame_index = 0  # Start from the first frame of the chosen set
        # car.frame_counter = 0  # Counter to control frame switching frequency
        car.shape(car.frames[car.frame_index])  # Set the initial frame shape

        # Set a random y position (lane) for the car
        y_position = random.randint(-200, 200)
        car.goto(-390, y_position)  # Start from the left of the screen
        self.all_cars.append(car)

    def animate_and_move_cars(self):
        # Animate and move each car forward in a single loop
        for car in self.all_cars:

            car.shape(car.frames[car.frame_index])
            car.frame_index = (car.frame_index + 1) % len(car.frames)
            car.forward(self.car_speed)

            # Remove cars that go off the screen to the right
            if car.xcor() > 290:
                car.hideturtle()
                self.all_cars.remove(car)

        # Update the screen for smooth animation
        self.screen.update()

    def increase_speed(self):
        self.car_speed += 3

    def run_game(self):
        if score.level == 1:
            if random.randint(1, 6) == 1:
                self.create_car()
        elif score.level == 2:
            if random.randint(1, 4) == 1:
                self.create_car()
        elif score.level == 3:
            if random.randint(1, 2) == 1:
                self.create_car()
        self.animate_and_move_cars()
        time.sleep(0.05)




