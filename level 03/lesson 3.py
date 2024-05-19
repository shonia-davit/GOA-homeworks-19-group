# 1)დაპრინტეთ თქვენი ოჯახის წევრების სახელები ტერმინალში 

mom = "dodo"
dad = "lasha"
brother1 = "zvio"
brother2 = "ilia"
brother3 = "gio"
grandmother = "nazi"
grandfather = "nodari"



print(mom)
print(dad)
print(brother1)
print(brother2)
print(brother3)
print(grandmother)
print(grandfather)  




########################################################################

# 2)turtle-ში დახატეთ ოთხი სახლიც, ეზოთი, მზეც, ხეებიც


from turtle import *


# i want to draw 4 house
#starting with a 1st square

color("purple")
speed(120)
width(7)
penup()
goto(170,100)
pendown()
begin_fill()
left(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
end_fill()

# drawing a roof of 1st square


right(90)
forward(150)
color("red")
begin_fill()
right(45)
forward(105)
right(90)
forward(105)
end_fill()

# drawing a 1st window of 1st square

color("yellow")
penup()
goto(185, 235)
pendown()
left(45)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(20)
right(90)
forward(35)


# drawing a 2nd window of a 1st square

penup()
goto(305,235)
pendown()
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(17.5)
right(90)
forward(40)

#  drawing a door of 1st square

penup()
color("green")
goto(230,100)
pendown()
begin_fill()
left(180)
forward(80)
right(90)
forward(30)
right(90)
forward(80)
end_fill()

# finished drawing 1st house


# drawing 2nd house


# drawing square of 2nd house


penup()
color("purple")
goto(-30,100)
pendown()
begin_fill()
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()


# drawing a roof of 2nd house


left(180)
forward(150)
right(45)
color("red")
begin_fill()
forward(105)
right(90)
forward(105)
end_fill()


# drawing 1st window of 2nd house

penup()
color("yellow")
goto(-15,235)
pendown()
left(45)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(20)
right(90)
forward(35)

# drawing a 2nd window of a 2nd house

penup()
goto(100,235)
pendown()
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(17.5)
right(90)
forward(40)


# drawing a door of 2nd house

penup()
color("green")
goto(30,100)
pendown()
begin_fill()
left(180)
forward(80)
right(90)
forward(30)
right(90)
forward(80)
end_fill()

# finished drawing a 2nd house


# drawing 3rd house

# drawing square of 3rd house


penup()
color("purple")
goto(-30,-200)
pendown()
begin_fill()
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
end_fill()


#  drawing a roof of 3rd square

right(180)
forward(150)
color("red")
begin_fill()
right(45)
forward(105)
right(90)
forward(105)
end_fill()


#  drawing 1st window of 3rd house

penup()
color("yellow")
goto(-15,-75)
pendown()
left(45)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(20)
right(90)
forward(35)


# drawing a 2nd window of 3rd house

penup()
goto(100,-75)
pendown()
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(17.5)
right(90)
forward(40)

#drawing a door of 3rd house

penup()
color("green")
goto(30,-200)
pendown()
begin_fill()
left(180)
forward(80)
right(90)
forward(30)
right(90)
forward(80)
end_fill()


# finished drawing 3rd house

# drawing 4th house

# drawing a square of 4th house

penup()
color("purple")
goto(170,-200)
pendown()
begin_fill()
left(180)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
right(90)
forward(150)
end_fill()


# #drawing a roof of 4th house

right(90)
forward(150)
color("red")
begin_fill()
right(45)
forward(105)
right(90)
forward(105)
end_fill()


#  drawing 1st window of 4th house

penup()
color("yellow")
goto(185,-70)
pendown()
left(45)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(40)
right(90)
forward(17.5)
right(90)
forward(20)
right(90)
forward(35)

# # drawing 2nd window of 4th square

penup()
goto(305,-70)
pendown()
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(40)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(35)
right(90)
forward(20)
right(90)
forward(17.5)
right(90)
forward(40)


# #drawing a door of 4th house

penup()
color("green")
goto(230,-200)
pendown()
begin_fill()
left(180)
forward(80)
right(90)
forward(30)
right(90)
forward(80)
end_fill()


# #finished drawing 4th house 

# drawing a sun

penup()
goto(-250 ,250)
pendown()
color("yellow")
begin_fill()
circle(50)


end_fill()




exitonclick()
