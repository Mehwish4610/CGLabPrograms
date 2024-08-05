import turtle
def bl(x1, y1, x2, y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    x_step = 1 if x1<x2 else -1
    y_step = 1 if y1<y2 else -1
    error = 2*dy -dx
    linepoints = []
    x,y = x1, y1
    for _ in range(dx+1):
        linepoints.append((x,y))
        if error>0:
            y += y_step
            error -= 2*dx
        x += x_step
        error += 2*dy
    return linepoints
turtle.setup(500,500)
turtle.speed(0)
x1, y1 = 100, 100
x2, y2 =400, 300
linepoints = bl(x1, y1, x2, y2)
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
for x,y in linepoints:
    turtle.goto(x,y)
turtle.exitonclick()