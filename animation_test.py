# import time
# from turtle import Turtle, Screen
# import random
# import os
#
#
# class AnimationTest:
#     def __init__(self):
#         self.all_car = []
#         self.start_move = 10
#         self.is_moving = False  # Flag to check if the car is moving
#         self.frames = [
#             "warrior/frame_0.gif", "warrior/frame_1.gif", "warrior/frame_2.gif", "warrior/frame_3.gif",
#             "warrior/frame_4.gif", "warrior/frame_5.gif", "warrior/frame_6.gif", "warrior/frame_7.gif"
#         ]
#
#         self.idle_frames = [
#             "idle/frame_0.gif", "idle/frame_1.gif", "idle/frame_2.gif", "idle/frame_3.gif",
#             "idle/frame_4.gif", "idle/frame_5.gif", "idle/frame_6.gif", "idle/frame_7.gif",
#             "idle/frame_8.gif", "idle/frame_9.gif"
#         ]
#
#         # self.frames = [
#         #     "jump/frame_0.gif", "jump/frame_1.gif", "jump/frame_2.gif"
#         # ]
#
#         self.screen = Screen()
#         self.screen.bgpic("blurred_background.gif")
#         self.screen.setup(width=500, height=500)
#         self.screen.tracer(0)
#
#         # Load all frames into the screen
#         for frame in self.frames + self.idle_frames:
#             if os.path.exists(frame):
#                 self.screen.addshape(frame)
#             else:
#                 print(f"Warning: Frame {frame} doesn't exist")
#
#         # Create the initial car
#         self.car_create()
#
#     def car_create(self):
#         car = Turtle()
#         car.shape(self.idle_frames[0])
#         car.penup()
#         car.goto(0, -280)
#         car.setheading(90)  # Set heading upwards
#         car.frame_index = 0
#         self.all_car.append(car)
#
#     def animate_cars(self):
#         # Animate cars based on movement status
#         for car in self.all_car:
#             frames = self.frames if self.is_moving else self.idle_frames  # Choose frames based on movement status
#             if car.frame_index >= len(frames):
#                 car.frame_index = 0
#             car.shape(frames[car.frame_index])  # Update to the next frame
#             car.frame_index = (car.frame_index + 1) % len(frames)  # Loop through frames
#
#         self.screen.update()  # Refresh the screen with new frames
#
#     def move_forward(self):
#         # Move cars forward and switch to movement frames
#         self.is_moving = True
#         for car in self.all_car:
#             car.frame_index = 0
#             car.setheading(90)
#             car.forward(self.start_move)
#
#     def move_left(self):
#         # Move cars left and switch to movement frames
#         self.is_moving = True
#         for car in self.all_car:
#             car.frame_index = 0
#             car.setheading(180)
#             car.forward(self.start_move)
#
#     def move_right(self):
#         self.is_moving = True
#         for car in self.all_car:
#             car.frame_index = 0
#             car.setheading(0)
#             car.forward(self.start_move)
#
#     def move_backward(self):
#         self.is_moving = True
#         for car in self.all_car:
#             car.frame_index = 0
#             car.setheading(270)
#             car.forward(self.start_move)
#
#
#     def stop_moving(self):
#         # Stop movement and switch back to idle frames
#         self.is_moving = False
#
#     def run_game(self):
#         while True:
#             self.animate_cars()  # Keep animating frames
#             time.sleep(0.09)  # Control animation speed
#
#
# # Set up key bindings and start the game
# class U:
#     screen = Screen()
#     game = AnimationTest()
#
#     # Bind keys for movement and stopping movement
#     screen.listen()
#
#     screen.onkeypress(fun=game.move_left, key="Left")
#     screen.onkeypress(fun=game.move_forward, key="Up")
#     screen.onkeypress(fun=game.move_right, key="Right")
#     screen.onkeypress(fun=game.move_backward, key="Down")
#
#
#
#     screen.onkeyrelease(game.stop_moving, "Down")  # Stop movement when releasing Left
#     screen.onkeyrelease(game.stop_moving, "Right")  # Stop movement when releasing Up
#     screen.onkeyrelease(game.stop_moving, "Up")
#     screen.onkeyrelease(game.stop_moving, "Left")
#
#     # Start the main game loop
#     game.run_game()
#     screen.exitonclick()
#

from turtle import Turtle, Screen
import random
import time
import os


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5  # Speed of car movement
        self.screen = Screen()
        self.screen.setup(width=400, height=500)
        self.screen.tracer(0)  # Turn off automatic screen updates for smoother animation

        self.fire_frames = [
            "knight/frame_0.gif", "knight/frame_1.gif", "knight/frame_2.gif", "knight/frame_3.gif",
            "knight/frame_4.gif", "knight/frame_5.gif", "knight/frame_6.gif", "knight/frame_7.gif"
        ]


        # Load frames as shapes
        for frames_list in [self.fire_frames]:
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
        car.frames = random.choice([self.fire_frames])
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
            # Update frame only every few iterations for smoother animation
            if not hasattr(car, 'frame_counter'):
                car.frame_counter = 0  # Initialize frame counter if it doesn't exist

            # Increment the frame counter each loop
            car.frame_counter += 1

            # Change the frame every 5 frames to control animation speed
            if car.frame_counter >= 1:
                car.frame_index = (car.frame_index + 1) % len(car.frames)  # Increment frame index within bounds
                car.shape(car.frames[car.frame_index])  # Set new frame shape
                car.frame_counter = 0  # Reset counter

            # Move forward
            car.forward(3)

            # Remove cars that go off the screen to the right
            if car.xcor() > 290:
                car.hideturtle()
                self.all_cars.remove(car)

        # Update the screen for smooth animation
        self.screen.update()

    def increase_speed(self):
        self.car_speed += 5

    def run_game(self):
        # Main game loop
        while True:
            if random.randint(1, 6) == 1:  # Roughly 1 in 6 chance to create a car per loop
                self.create_car()

                # Animate and move each car
            self.animate_and_move_cars()

                # Small delay to control game speed
            time.sleep(0.05)





car = Car()
car.run_game()