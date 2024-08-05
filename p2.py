import turtle
import math
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(1)
t.pensize(2)
def d_rec(x, y, w, h, color ):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
def d_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y-radius)
    t.pendown()
    t.color(color)
    t.circle(radius)
def translate(x, y, dx, dy):
    t.penup()
    t.goto(x+dx, y+dy)
    t.pendown()
def rotate(x, y, angle):
    t.penup()
    t.goto(x,y)
    t.setheading(angle)
    t.pendown()
def scale(x, y, sx, sy):
    t.penup()
    t.goto(x*sx, y*sy)
    t.pendown()
d_rec(-200, 0,100,50, "blue")
translate(-200, 0, 200, 0)
d_rec(0,0,100,50,"blue")
rotate(0,0,45)
d_rec(0,0,100,50,"blue")
scale(0,0,2,2)
d_rec(0,0,200,100,"blue")
d_circle(100,100,50,"red")
translate(100,100,200,0)
d_circle(300,100,50,"red")
rotate(0,0,30)
d_circle(300,100,50,"red")
scale(300,100,2,2)
d_circle(600,200,100,"red")
turtle.done()