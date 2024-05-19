from turtle import *



speed(20)

width(6)

# want to draw a house

# drawing a square


color("purple")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)

end_fill()

penup()
goto(200, 200)
pendown()

# finished drawing a square


# drawing a roof ( tringle )

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# finished drawing a roof



# drawing a door

color("purple")
left(30)
forward(200)
left(90)
forward(70)
left(90)
color("yellow")
begin_fill()
forward(120)
right(90)
forward(70)
right(90)
forward(120)
end_fill()

# finished drawing a door

# drawing 1st window


penup()
goto(175, 175)
pendown()
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
left(90)
forward(20)
left(90)
forward(25)
left(90)
forward(40)

# finished drawing 1st window

# drawing  2nd window

penup()
goto(25, 175)
pendown()
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(25)
right(90)
forward(40)
right(90)
forward(25)
right(90)
forward(20)
right(90)
forward(50)


# finished drawing 2nd window

# our house is done    





exitonclick()