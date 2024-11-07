from turtle import Turtle

# Updated font style and size
FONT = ("Courier", 26)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        # self.game_over = pygame.mixer.Sound('music/game-over.wav')
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 200)
        # self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):

        self.goto(0, 0)
        self.color("red")  # Set the text color to red
        self.write("Game Over", align="center", font=("Courier", 48, "bold"))  # Larger, bolder font
        # self.game_over.play()
