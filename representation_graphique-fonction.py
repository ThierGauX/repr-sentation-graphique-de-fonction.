from turtle import *
import turtle
import time


turtle.screensize(1500, 1500)
x = 0


def tableau():
    title("representation graphique fonction")
    turtle.bgcolor("black")
    color("white")
    home()
    turtle.speed(50)
    angle = -90 
    for i in range(4):
        home()
        right(angle)
        for i in range(20):
            forward(20)
            grad()
        angle += 90


def grad():
    left(90)
    forward(5)
    back(10)
    forward(5)
    right(90)



def afficher(absy, ordo):
    
    pendown()  
    color("red")
    goto(absy*20, ordo*20)
    pendown()
    color('blue')
    right(-45)
    forward(5)
    forward(-10)
    forward(5)
    left(-90)
    forward(5)
    forward(-10)
    

def fonction(x):
    color("red")
    for i in range(-20, 21):
        x = (i**2)+1
        afficher(i, x)
        


    



tableau()
fonction(x)
time.sleep(40)