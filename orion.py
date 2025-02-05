# this program is going to draw the stars of the orion constellation.
# as well as the name of the stars + constellation lines.
import turtle

#setting window size
turtle.setup(500, 600)

#setting up turtle
turtle.penup()
turtle.hideturtle()

#creating named constants for the star coordinates
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

#drawing the stars
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)    #THIS IS THE LEFT SHOULDER
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  #THIS IS THE RIGHT SHOULDER
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)    #THIS IS THE LEFT BELT STAR
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #THIS IS THE MIDDLE BELT STAR
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)  #THIS IS THE RIGHT BELT STAR
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)            #THIS IS THE LEFT KNEE
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)          #THIS IS THE RIGHT KNEE
turtle.dot()

#displaying the star names
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)   #this is the left shoulder
turtle.write('Betelgeuse')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #this is the right shoulder
turtle.write('Meissa')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)   #left beltstar
turtle.write('Alnitak')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  #middle beltstar
turtle.write('Alnilam')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)  #right beltstar
turtle.write('Mintaka')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)    #left knee
turtle.write('Saiph')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  #right knee
turtle.write('Rigel')

#drawing a line from left shoulder to left beltstar
turtle.goto(LEFT_SHOULDER_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

#drawling a line from the right shoulder to right beltstar
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

#drawing a line from left beltstar to middle beltstar
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

#drawing a line for the middle beltstar to right beltstar
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

#drawing a line from left beltsar to left knee
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

#drawing a line from right beltstar to right knee
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

#keeping the window open
turtle.done