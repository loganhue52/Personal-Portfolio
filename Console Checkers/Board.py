import turtle as t

class Board:
    def __init__(self,wn):
        self.t=t.Turtle()
        self.wn=wn

    def drawBoard(self):
        #getting the turtle set up
        self.t.speed(0)
        self.t.up()
        self.t.hideturtle()
        self.t.goto(-350,350)
        self.t.setheading(0)
        ls=0
        #custom colors picked because normal red and black hurt my eyes
        red="#c42b2b"
        black='#232323'
        color=red
        self.t.shape('square')
        self.t.color(color)
        self.t.shapesize(5)
        #8 rows
        for i in range(8):
            #8 squares per row
            for i in range(8):
                self.t.color(color)
                #piece stamps
                self.t.stamp()
                #moves forward 100
                self.t.fd(100)
                #switches color between sqaures
                if color==red:
                    color=black
                else:
                    color=red
            #then switches color between rows to keep them alternated
            if color==red:
                color=black
            else:
                color=red
            #then the ls variable is used to move the turtle down 100 every row
            ls+=100
            self.t.goto(-350,350-ls)
            self.t.setheading(0)