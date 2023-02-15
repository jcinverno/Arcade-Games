# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:23:14 2021

@author: jcinv
"""

from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
screen.setup(width = 500, height = 400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
position = [-140, -80, -30, 30, 80, 140]
player = [] 

for e in range(len(colors)):
    
    t = Turtle(shape='turtle')
    t.color(colors[e])
    t.penup()
    t.goto(x = -240, y = position[e])
    t.speed('fastest')
    player.append(t)
 
if user_bet:
    is_race_on = True 
    
while is_race_on:
    
    for e in player:
        
        place = e.xcor()
        if place >= 230:
            is_race_on = False
            winning_color = e.fillcolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} won.")
            else:
                print(f"You've lost! The {winning_color} won.")
        else:
            dist = randint(0, 5)
            e.forward(dist)
        

        
        
            

            
        
        
        
        
        
        
        
        

screen.exitonclick()
