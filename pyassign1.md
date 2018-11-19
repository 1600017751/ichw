#!/usr/bin/env python3

"""Planets.py: Description of how solar system runs.

__author__ = "Ye Weiting"
__pkuid__  = "1600017751"
__email__  = "1600017751@pku.edu.cn"
"""

import turtle
import math
sc=turtle.Screen()
sc.screensize(2020,2000)
Sun=turtle.Turtle()
Mercury=turtle.Turtle()
Venus=turtle.Turtle()
Earth=turtle.Turtle()
Mars=turtle.Turtle()
Jupiter=turtle.Turtle()
Saturn=turtle.Turtle()
"""build all the planets
"""

Sun.shape("circle")
Mercury.shape("circle")
Venus.shape("circle")
Earth.shape("circle")
Mars.shape("circle")
Jupiter.shape("circle")
Saturn.shape("circle")
Sun.color("orange")
Mercury.color("black")
Venus.color("yellow")
Earth.color("blue")
Mars.color("red")
Jupiter.color("green")
Saturn.color("brown")
Mercury.pencolor("black")
Venus.pencolor("yellow")
Earth.pencolor("blue")
Mars.pencolor("red")
Jupiter.pencolor("green")
Saturn.pencolor("brown")
"""set the shape and color
"""

Mercury.up()
Mercury.setpos(47,0)
Mercury.pendown()
Venus.up()
Venus.setpos(73,0)
Venus.pendown()
Earth.up()
Earth.setpos(102,0)
Earth.pendown()
Mars.up()
Mars.setpos(167,0)
Mars.pendown()
Jupiter.up()
Jupiter.setpos(546,0)
Jupiter.pendown()
Saturn.up()
Saturn.setpos(1010,0)
Saturn.pendown()
"""set the initial position
"""

for i in range(1,10768):
    """set the speed and course
    """
    xMercury=8+39*math.cos(i/44*math.pi)
    yMercury=38*math.sin(i/44*math.pi)
    Mercury.setpos(xMercury,yMercury)
    xVenus=0.5+72.5*math.cos(i/112*math.pi)
    yVenus=72.5*math.sin(i/112*math.pi)
    Venus.setpos(xVenus,yVenus)
    xEarth=2+100*math.cos(i/182*math.pi)
    yEarth=99.7*math.sin(i/182*math.pi)
    Earth.setpos(xEarth,yEarth)
    xMars=14.5+152.5*math.cos(i/344*math.pi)
    yMars=151.9*math.sin(i/344*math.pi)
    Mars.setpos(xMars,yMars)
    xJupiter=25.5+520.5*math.cos(i/2154*math.pi)
    yJupiter=520*math.sin(i/2154*math.pi)
    Jupiter.setpos(xJupiter,yJupiter)
    xSaturn=55+955*math.cos(i/5384*math.pi)
    ySaturn=953.1*math.sin(i/5384*math.pi)
    Saturn.setpos(xSaturn,ySaturn)    
