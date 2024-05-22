from turtle import *


# turtle-შო დახაზეთ სასახლე, მეფე და 
# დედოფალი, დაარჭვეთ GOA-ს 
# დროშა კოშკზე.
# (ფანტაზია თქვენით)


bgcolor("green")

# drawing a castle

width(7)

speed(11111111111111)

color("gray")

begin_fill()

penup()
goto(-300 , -300)
pendown()
forward(590)
left(90)
forward(450)
left(90)
forward(50)

color("gray")

penup()
goto(240,150)
pendown()

forward(40)
left(90)
forward(170)
right(90)
forward(50)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
right(90)
forward(20)
right(90)
forward(200)
right(90)
forward(40)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
right(90)
forward(480)
left(90)
forward(30)

end_fill()

#  finished drawing a castle

#  drawing a flag

color("black")

penup()
goto(200 , 150)
pendown()

begin_fill()

forward(120)
left(130)
forward(120)
left(100)
forward(120)
left(130)
forward(50)

end_fill()

color("white")

penup()
forward(27)
left(90)
forward(97)
pendown()
forward(80)
right(90)
color("black")
begin_fill()
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
color("green")

penup()
goto(260, 300)
pendown()

left(180)
forward(15)
right(90)
forward(15)
right(90)
forward(25)
right(90)
forward(30)
right(90)
forward(25)

penup()
forward(13)
pendown()

forward(20)
right(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)

penup()
goto(320 , 285)
pendown()

forward(30)
right(90)
forward(20)
right(90)
forward(30)
left(180)
forward(15)
left(90)
forward(20)

#  finished drawing a flag 

#  drawing an entrance to the castle

penup()
goto(-125 , -305)
pendown()

color("brown")
begin_fill()
right(90)
forward(170)
right(90)
forward(200)
right(90)
forward(170)
end_fill()
penup()
right(90)
forward(100)
pendown()
color("black")
right(90)
forward(170)
right(90)
forward(100)
right(90)
forward(170)
right(90)
forward(200)
right(90)
forward(170)
right(90)
forward(100)

#  finished drawing entrance of castle

#  drawing king

color("black")

penup()
goto(-100 ,-20 )
pendown()
left(85)
forward(130)
right(140)
forward(60)
right(35)
forward(40)

penup()
goto(-100 , -20)
pendown()

left(175)
forward(130)
left(5)
forward(50)
right(140)
forward(60)
left(180)
forward(60)
left(100)
forward(60)
right(180)
forward(60)
left(40)
forward(10)

penup()
forward(30)
right(90)
forward(30)
pendown()

left(90)


circle(30)

penup()
goto(-100 , 235)
pendown()

width(4)

color("yellow")

right(90)
forward(30)
left(90)
forward(20)
left(140)
forward(10)
right(90)
forward(10)
left(90)
forward(10)
right(90)
forward(10)
left(90)
forward(10)
right(90)
forward(10)
left(140)
forward(20)
left(90)
forward(40)


width(7)



#  finished drawing the king


#  drawing the queen

penup()
goto(100, -20)
pendown()

color("black")

left(90)
forward(130)
left(140)
forward(60)
left(30)
forward(30)

penup()
goto(100, -20)
pendown()

right(170)
forward(130)
right(10)
forward(60)
left(140)
forward(60)
left(180)
forward(60)
right(100)
forward(60)
right(180)
forward(60)
right(40)
forward(5)

penup()
forward(30)
right(90)
forward(30)
pendown()

left(90)


circle(30)



exitonclick()