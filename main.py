import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.add_car()
    screen.update()
    
    cars.move_cars()
    
    for c in cars.car_list:
        if player.distance(c) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    if player.ycor() > 280:
        player.next_level()
        scoreboard.level_up()
        cars.level_up()
        
screen.exitonclick()