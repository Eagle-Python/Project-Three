from turtle import Screen, Turtle
import subprocess
import pygame

screen = Screen()
screen.setup(width=600, height=500)

# Start screen elements
start_text = Turtle()
start_text.hideturtle()
play_button = Turtle()
play_button.shape("square")
play_button.color("green")
play_button.shapesize(stretch_wid=2, stretch_len=5)
play_button.penup()
play_button.goto(0, 0)

def start_game(x, y):
    # Check if the play button was clicked
    if -50 < x < 50 and -20 < y < 20:
        screen.bye()  # Close the start screen
        subprocess.run(["python", "main.py"])  # Run the main game

# Display the start screen
start_text.write("Press 'Play' to Start", align="center", font=("Arial", 24, "bold"))
play_button.onclick(start_game)  # Add click event for the play button

screen.mainloop()
