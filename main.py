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



def afficher(absy, ordo, c):
    if c == 1:
        color("red")
    if c == 2:
        color("green")
    if c == 3:
        color("blue")
    if c == 4:
        color("orange")
    pendown()  
    goto(absy*20, ordo*20)
    pendown()
    right(-45)
    forward(5)
    forward(-10)
    forward(5)
    left(-90)
    forward(5)
    forward(-10)
    forward(5)
    

def fonction(x):
    c = 1
    color("red")
    for i in range(-20, 21):
        x = (i**2)-20
        afficher(i, x, c)
        
def fonction2(x):
    c = 2
    color("red")
    for i in range(-20, 21):
        x = (i**2)-10
        afficher(i, x, c)

def fonction3(x):
    c = 3
    color("red")
    for i in range(-20, 21):
        x = (i**2)
        afficher(i, x, c)

def fonction4(x):
    c = 4
    color("red")
    for i in range(-20, 21):
        x = (i**2)+10
        afficher(i, x, c)    



tableau()
fonction(x)
fonction2(x)
fonction3(x)
fonction4(x)
time.sleep(40)
