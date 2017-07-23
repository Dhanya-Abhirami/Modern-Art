from turtle import * # imports the module turtle,
                    
from random import randint
speed(0) # sets the speed of drawing to 0, which is the fastest
colormode(255)

bgcolor('black') # sets the color of the background/canvas to black

x = 0 # creates a variable x with value 0
up() # lifts up the pen, so no lines are drawn

#note fd() means move forward, bk() means move back
# rt() or lt() means tilt right by a certain angle
rt(45) 
fd(90) 
rt(120) 

down() # sets down the pen, so that turtle can draw
while x < 100: # while the value of x is lesser than 120,
                #continuously do this:
    pencolor(randint(0,255),randint(0,255),randint(0,255))
    fd(200)     
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)
    fd(200)
    rt(61)

    rt(11) 
    x = x+1 # adds 1 to the value of x,
            # so that it is closer to 120 after every loop

exitonclick() # When you click, turtle exits.
