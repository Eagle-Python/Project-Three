from turtle import Turtle, Screen
import os
import time
import pygame

move_direction = 90
move_distance = 200
start_direction = (0, -200)
end_direction = 270


class Player:
    def __init__(self):
        self.jump_sound = pygame.mixer.Sound('music/jump.wav')
        self.left = pygame.mixer.Sound('music/left.wav')
        self.right = pygame.mixer.Sound('music/right.flac')
        self.sword = pygame.mixer.Sound('music/sword.flac')
        self.runner = []
        self.start_move = 10
        self.is_moving = False  # Flag to check if the car is moving
        self.run_frames = [
            "main_hero/run/frame_0.gif", "main_hero/run/frame_1.gif", "main_hero/run/frame_2.gif", "main_hero/run/frame_3.gif",
            "main_hero/run/frame_4.gif", "main_hero/run/frame_5.gif", "main_hero/run/frame_6.gif"
        ]

        self.idle_frames = [
            "main_hero/idle/frame_0.gif", "main_hero/idle/frame_1.gif", "main_hero/idle/frame_2.gif", "main_hero/idle/frame_3.gif",
        ]

        self.fight_frames = [
            "main_hero/fight/frame_0.gif", "main_hero/fight/frame_1.gif", "main_hero/fight/frame_2.gif",
            "main_hero/fight/frame_3.gif"
        ]
        self.fight_one_frames = [
            "main_hero/fight_one/frame_0.gif", "main_hero/fight_one/frame_1.gif", "main_hero/fight_one/frame_2.gif",
            "main_hero/fight_one/frame_3.gif"
        ]
        self.death_frames = [
            "main_hero/death/frame_2.gif",
            "main_hero/death/frame_3.gif", "main_hero/death/frame_4.gif", "main_hero/death/frame_5.gif",
            "main_hero/death/frame_6.gif"
        ]
        # Current action to decide which frames to use
        self.current_action = "idle"  # Start with idle state

        self.screen = Screen()
        self.screen.tracer(0)

        # Load all frames into the screen
        for frame in self.run_frames + self.idle_frames + self.fight_frames + self.death_frames + self.fight_one_frames:
            if os.path.exists(frame):
                self.screen.addshape(frame)
            else:
                print(f"Warning: Frame {frame} doesn't exist")

        # Create the initial car
        self.car_create()

    def car_create(self):
        car = Turtle()
        car.shape(self.idle_frames[0])
        car.penup()
        car.goto(start_direction)
        car.setheading(90)  # Set heading upwards
        car.frame_index = 0
        self.runner.append(car)

    def start(self):
        for car in self.runner:
            car.goto(start_direction)

    def animate_cars(self):
        # Animate cars based on movement status
        for car in self.runner:
            # Determine frames based on current action
            if self.current_action == "idle":
                frames = self.idle_frames
            elif self.current_action == "running":
                frames = self.run_frames
            elif self.current_action == "fighting":
                frames = self.fight_frames
            elif self.current_action == "fighting_one":
                frames = self.fight_one_frames
            elif self.current_action == "death":
                frames = self.death_frames

            # frames = self.run_frames if self.is_moving else self.idle_frames  # Choose frames based on movement status
            if car.frame_index >= len(frames):
                car.frame_index = 0
            car.shape(frames[car.frame_index])  # Update to the next frame
            car.frame_index = (car.frame_index + 1) % len(frames)  # Loop through frames

        self.screen.update()  # Refresh the screen with new frames

    def move_forward(self):
        # Move cars forward and switch to movement frames
        self.current_action = "running"
        for car in self.runner:
            car.frame_index = 0
            car.setheading(90)
            car.forward(self.start_move)
        self.jump_sound.play()

    def move_left(self):
        # Move cars left and switch to movement frames
        self.current_action = "running"
        for car in self.runner:
            if car.xcor() > -250:
                car.frame_index = 0
                car.setheading(180)
                car.forward(self.start_move)
        self.right.play()

    def move_right(self):
        self.current_action = "running"
        for car in self.runner:
            if car.xcor() < 250:
                car.frame_index = 0
                car.setheading(0)
                car.forward(self.start_move)
        self.right.play()

    def move_backward(self):
        self.current_action = "running"
        for car in self.runner:
            if car.ycor() > -200:
                car.frame_index = 0
                car.setheading(270)
                car.forward(self.start_move)

    def stop_moving(self):
        self.current_action = "idle"
        # Stop movement and switch back to idle frames

    def fight(self):
        self.current_action = "fighting"
        for car in self.runner:
            car.frame_index = 0
        self.sword.play()

    def fight_one(self):
        self.current_action = "fighting_one"
        for car in self.runner:
            car.frame_index = 0
        self.sword.play()

    def death(self):
        self.current_action = "death"
        for car in self.runner:
            car.frame_index = 0
            time.sleep(0)

    def runner_player(self):
        # while True:
        self.animate_cars()  # Keep animating frames
        time.sleep(0.05)  # Control animation speed

    def finish_line(self):
        for car in self.runner:
            if car.ycor() > end_direction:
                return True
            else:
                return False
