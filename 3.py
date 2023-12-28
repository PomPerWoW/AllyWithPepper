import turtle

class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    
    def showdisk(self):
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()
        turtle.setheading(0)  
        turtle.forward(self.dwidth / 2)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth)
        turtle.left(90)
        turtle.forward(self.dheight)
        turtle.left(90)
        turtle.forward(self.dwidth / 2)
        turtle.hideturtle()
        
    def newpos(self,xpos,ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
    def cleardisk(self):
        turtle.setheading(0) 
        turtle.penup()
        turtle.goto(self.dxpos, self.dypos)
        turtle.pendown()
        turtle.clear()
        turtle.setheading(0)  
        turtle.goto(self.dxpos, self.dypos)
        
# Example usage:
# Create a Disk object
disk = Disk(name="Disk1", xpos=0, ypos=0, height=20, width=40)

# Show the disk
disk.showdisk()

# Move the disk to a new position
disk.newpos(xpos=100, ypos=100)

# Show the disk at the new position
disk.showdisk()

# Clear the disk from the screen
disk.cleardisk()

# Keep the window open
turtle.mainloop()
