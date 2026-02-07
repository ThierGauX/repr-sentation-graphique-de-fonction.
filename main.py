from turtle import *
import math


f1 = lambda x: 150 * math.sin(x * 0.03)                
f2 = lambda x: 100 * math.cos(x * 0.05)               
f3 = lambda x: (x**2) / 100 - 200                      
f4 = lambda x: 50 * math.sin(x * 0.1) + (x * 0.5)      

fonctions = [f1, f2, f3, f4]
couleurs = ["cyan", "magenta", "yellow", "white"]

setup(1000, 800)
bgcolor("black")
speed(10) 
shape("circle")
turtlesize(0.7)

def tracer_axes():
    color("gray")
    width(1)
    
    penup(); goto(-500, 0); pendown(); goto(500, 0)
    
    penup(); goto(0, -400); pendown(); goto(0, 400)

tracer_axes()


for i in range(len(fonctions)):
    f = fonctions[i]
    color(couleurs[i])
    width(2)
    
    
    penup()
    x_debut = -500
    goto(x_debut, f(x_debut))
    pendown()
    
    
    for x in range(-500, 501, 5):
        y = f(x)
        goto(x, y)

hideturtle() 
done()
