import time
from turtle import Screen
from player import Player
from car import Car
from score import Score
import pygame

pygame.mixer.init()
pygame.mixer.music.load('music/bk.wav')
# ha_sound = pygame.mixer.Sound('music/ha.wav')
game_over = pygame.mixer.Sound('music/game-over.wav')
clapping = pygame.mixer.Sound('music/clapping.wav')
pygame.mixer.music.play(-1)

screen = Screen()
screen.bgpic("background/l1.gif")
screen.setup(width=600, height=500)
screen.tracer(0)


car = Car()
player = Player()
score = Score()

score.update_level()

screen.listen()
screen.onkeypress(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_forward, key="Up")
screen.onkeypress(fun=player.move_right, key="Right")
screen.onkeypress(fun=player.move_backward, key="Down")
screen.onkeypress(fun=player.fight, key="k")
screen.onkeypress(fun=player.fight_one, key="j")

screen.onkeyrelease(player.stop_moving, "Down")
screen.onkeyrelease(player.stop_moving, "Right")  # Stop movement when releasing Up
# screen.onkeyrelease(player.stop_moving, "Up")
screen.onkeyrelease(player.stop_moving, "Left")  # Stop movement when releasing Left
screen.onkeyrelease(player.stop_moving, 'k')
screen.onkeyrelease(player.stop_moving, 'j')


is_game = True
while is_game:
    print(score.level)
    if score.level == 2:
        screen.bgpic('background/l2.gif')
    elif score.level == 3:
        screen.bgpic('background/l4.gif')
    elif score.level == 4:
        screen.bgpic('background/l3.gif')
    screen.update()

    # for creating Car
    car.run_game()
    player.runner_player()

    for players in player.runner:
        for cars in car.all_cars:
            if cars.distance(players) < 25:
                player.death()
                game_over.play()
                score.game_over()
                time.sleep(0.5)

                if cars.distance(players) < 25:

                    is_game = False

    if player.finish_line():
        player.start()
        clapping.play()
        car.increase_speed()
        score.increase_level()


pygame.mixer.music.stop()
pygame.mixer.quit()
screen.exitonclick()