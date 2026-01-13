import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("pluto and charon awww")

#constant variables
plutomass = 1.0
charonmass = 0.12
distance = 200 #pixel
anglespeed = 0.01 #radians, per frame basically

barycenter_offset = (charonmass / (plutomass + charonmass)) * distance

pluto_orbitradius = barycenter_offset
charon_orbitradius = distance - barycenter_offset

class body:
    def __init__(self, radius, color, trailcolor):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.shapesize(radius / 10)
        self.turtle.penup()
        # orbit path
        self.trail = turtle.Turtle()
        self.trail.hideturtle()
        self.trail.color(trailcolor)
        self.trail.penup()

        self.first_move = True


    def move_to(self, x, y):
        self.turtle.goto(x,y)

        if self.first_move:
            self.trail.goto(x,y)
            self.trail.pendown()
            self.first_move = False
        else:
            self.trail.goto(x,y)

pluto = body(radius=20, color="brown", trailcolor="white")
charon = body(radius=12, color="gray", trailcolor="gray")

barycenter = turtle.Turtle()
barycenter.shape("circle")
barycenter.color("white")
barycenter.shapesize(.03)
barycenter.penup()
barycenter.goto(0,0)

angle = 0

while True:
    angle += anglespeed

    pluto_x = -barycenter_offset * math.cos(angle)
    pluto_y = -barycenter_offset + math.sin(angle)

    charon_x = (distance - barycenter_offset) * math.cos(angle)
    charon_y = (distance - barycenter_offset) * math.sin(angle)

    pluto.move_to(pluto_x, pluto_y)
    charon.move_to(charon_x, charon_y)

    time.sleep(0.01)
