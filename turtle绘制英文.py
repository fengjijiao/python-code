#! /usr/bin/env python
# coding=utf-8

import turtle,math

turtle.setup(1200,800)

#将海龟移动到靠左上
turtle.penup()
turtle.goto(-500,300)
turtle.pendown()

turtle.pencolor("cyan")
turtle.pensize(8)
#F
turtle.fd(-50)
turtle.seth(-90)
turtle.fd(50)
turtle.seth(-180)
turtle.fd(-50)
turtle.fd(50)
turtle.seth(-90)
turtle.fd(50)


turtle.penup()

turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()

#E
turtle.fd(-50)
turtle.seth(-90)
turtle.fd(50)
turtle.seth(0)
turtle.fd(50)
turtle.fd(-50)
turtle.seth(-90)
turtle.fd(50)
turtle.seth(0)
turtle.fd(50)

turtle.penup()

turtle.fd(-50)
turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()

#N

turtle.seth(-90)
turtle.fd(100)
turtle.seth(117)
turtle.fd(math.sqrt(math.pow(100,2)+math.pow(50,2)))
turtle.seth(-90)
turtle.fd(100)

turtle.penup()

turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()

#G
turtle.fd(-50)
turtle.seth(-90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(50)
turtle.seth(90)
turtle.fd(50)
turtle.seth(180)
turtle.fd(25)

turtle.fd(-25)
turtle.seth(-90)
turtle.fd(50)
turtle.seth(180)
turtle.fd(50)


turtle.penup()

turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()


#J
turtle.seth(180)
turtle.fd(50)
turtle.fd(-25)
turtle.seth(-90)
turtle.fd(100)
turtle.seth(180)
turtle.fd(25)
turtle.seth(90)
turtle.fd(25)

turtle.penup()

turtle.fd(-25)
turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()

#I
turtle.seth(180)
turtle.fd(50)
turtle.fd(-25)
turtle.seth(-90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(25)
turtle.fd(-50)

turtle.penup()

turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()


#J
turtle.seth(180)
turtle.fd(50)
turtle.fd(-25)
turtle.seth(-90)
turtle.fd(100)
turtle.seth(180)
turtle.fd(25)
turtle.seth(90)
turtle.fd(25)

turtle.penup()

turtle.fd(-25)
turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()

#I
turtle.seth(180)
turtle.fd(50)
turtle.fd(-25)
turtle.seth(-90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(25)
turtle.fd(-50)

turtle.penup()

turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)
turtle.fd(-25)

turtle.pendown()

#a
turtle.seth(-104)
turtle.fd(math.sqrt(math.pow(25,2)+math.pow(100,2)))
turtle.fd(-math.sqrt(math.pow(25,2)+math.pow(100,2))/2)
turtle.seth(0)
turtle.fd(25)
turtle.fd(-25)
turtle.seth(-104)
turtle.fd(-math.sqrt(math.pow(25,2)+math.pow(100,2))/2)
turtle.seth(-76)
turtle.fd(math.sqrt(math.pow(25,2)+math.pow(100,2)))

turtle.penup()
turtle.seth(180)
turtle.fd(50)
turtle.seth(90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(130)

turtle.pendown()

#o
turtle.seth(180)
turtle.fd(50)
turtle.seth(-90)
turtle.fd(100)
turtle.seth(0)
turtle.fd(50)
turtle.seth(90)
turtle.fd(100)
turtle.done()