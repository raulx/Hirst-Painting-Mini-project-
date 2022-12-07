from turtle import Turtle,Screen
import random

def draw(tim):
    """ This function draws a new colored dot on screen."""
    new_color = random.choice(colors)
    tim.dot(20,new_color)
    tim.penup()
    tim.forward(30)
    tim.pendown()


def new_pos(tim):
    """ This function sets the starts position of turtle and also sends the turtle to new line after drawing one line."""
    global start_x, start_y
    tim.penup()
    tim.goto(start_x, start_y)
    tim.pendown()


def run_loop(tim):
    """ This loop draws a single a line of ten colored dot"""
    for i in range(10):
        draw(tim)


screen = Screen()
tim = Turtle()

screen.title("Hirst Painting.")
screen.screensize(400,300)

colors = ['red', 'yellow', 'green','blue', 'orange','brown','violet','silver','gray','pink']
start_x = -100
start_y = -70


for i in range(10):
    new_pos(tim)
    run_loop(tim)
    start_y += 30


screen.exitonclick()