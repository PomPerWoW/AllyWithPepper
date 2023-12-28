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
        

turtle.mainloop()

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100) -> None:
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length
    
    def showpole(self):
        turtle.goto(self.pxpos, self.pypos)
        turtle.fd(self.pthick)
        turtle.left(90)
        turtle.fd(self.plength)
        turtle.left(90)
        turtle.fd(self.pthick)
        turtle.left(90)
        turtle.fd(self.plength)
        turtle.left(90)
          
    def pushdisk(self, disk):
        self.stack.append(disk)
        disk.showdisk()
        self.toppos += 1
    
    def popdisk(self):
        disk = self.stack.pop()
        disk.cleardisk()
        self.toppos -= 1
        return disk

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, 0)
        self.workspacep = Pole(workspace, 150, 0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.destinationp.showpole(n)
        for i in range(n):
            self.startp.pushdisk(Disk("d"+str(i), 0, i*150, 20, (n-i)*30))
    
    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n-1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n-1, w, d, s)
        
    def solve(self):
        self.move_tower(3, self.startup, self.destinationp, self.workspace)

h = Hanoi()
h.solve()
