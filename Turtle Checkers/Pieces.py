import turtle as t

class Pieces:
    def __init__(self,wn):
        self.wn=wn
        #lists for movement checking
        self.piecelist=[]
        self.redlist=[]
        self.blacklist=[]
        #setting up every turtle, adding the image, then putting it in my piece list
        self.r1=t.Turtle()
        self.r1.shape('redChecker.gif')
        self.piecelist.append(self.r1)
        self.r2=t.Turtle()
        self.r2.shape('redChecker.gif')
        self.piecelist.append(self.r2)
        self.r3=t.Turtle()
        self.r3.shape('redChecker.gif')
        self.piecelist.append(self.r3)
        self.r4=t.Turtle()
        self.r4.shape('redChecker.gif')
        self.piecelist.append(self.r4)
        self.r5=t.Turtle()
        self.r5.shape('redChecker.gif')
        self.piecelist.append(self.r5)
        self.r6=t.Turtle()
        self.r6.shape('redChecker.gif')
        self.piecelist.append(self.r6)
        self.r7=t.Turtle()
        self.r7.shape('redChecker.gif')
        self.piecelist.append(self.r7)
        self.r8=t.Turtle()
        self.r8.shape('redChecker.gif')
        self.piecelist.append(self.r8)
        self.b1=t.Turtle()
        self.b1.shape('blackChecker.gif')
        self.piecelist.append(self.b1)
        self.b2=t.Turtle()
        self.b2.shape('blackChecker.gif')
        self.piecelist.append(self.b2)
        self.b3=t.Turtle()
        self.b3.shape('blackChecker.gif')
        self.piecelist.append(self.b3)
        self.b4=t.Turtle()
        self.b4.shape('blackChecker.gif')
        self.piecelist.append(self.b4)
        self.b5=t.Turtle()
        self.b5.shape('blackChecker.gif')
        self.piecelist.append(self.b5)
        self.b6=t.Turtle()
        self.b6.shape('blackChecker.gif')
        self.piecelist.append(self.b6)
        self.b7=t.Turtle()
        self.b7.shape('blackChecker.gif')
        self.piecelist.append(self.b7)
        self.b8=t.Turtle()
        self.b8.shape('blackChecker.gif')
        self.piecelist.append(self.b8)
        #setting the attributes for every turtle using the list
        for i in self.piecelist:
            i.speed(9)
            i.shapesize(4)
        #these are the white dots you will see when you click a turtle
        #they act as placeholders, click on them to move the turtle
        #down left
        self.DL=t.Turtle()
        #down right
        self.DR=t.Turtle()
        #up left
        self.UL=t.Turtle()
        #up right
        self.UR=t.Turtle()
        self.movers=[self.DL,self.DR,self.UL,self.UR]
        #setting the mover attributes
        for i in self.movers:
            i.color('white')
            i.shape('circle')
            i.up()
            i.speed(0)
            i.hideturtle()
        self.kinglist=[]

    #placing all of the pieces in inital locations
    #yes we only did 2 rows because it was easier to deal with
    def placePieces(self):
        num=0
        x,y=-250,350
        #for each piece
        for i in self.piecelist:
            #if it is less than 8, it is red and goes on tops
            if num<8:
                #if it equals 4 then it goes a row down
                if num==4:
                    x,y=-350,250
                #pieces moves to location
                i.up()
                i.goto(x,y)
                #x+=200 so that it skips a space
                x+=200
                self.redlist.append(i)
            else:
                #basically the same thing here
                if num==8:
                    x,y=-250,250
                if num==12:
                    x,y=-350,350
                i.up()
                i.goto(x,-y)
                x+=200
                self.blacklist.append(i)
            num+=1
                
        return self.piecelist,self.redlist,self.blacklist

    def moveCheck(self,x,y):
        self.moverclicked=""
        #x,y is cursor click location
        #grabbing which piece was clicked
        currentpiece=None
        for i in self.piecelist:
            if i.distance(x,y)<50:
                currentpiece=i

        #ah yes, a function within a function
        def move(x,y):

            for i in self.movers:
                #this is for getting precise movements to the exact middle of the squares
                if i.distance(x,y)<20:
                    currentpiece.goto(i.xcor(),i.ycor())
                    self.moverclicked=i
                i.hideturtle()

            #these statements tell when a piece needs to be a king and changes the image
            if currentpiece in self.redlist:
                if currentpiece.ycor()<-300:
                    self.kinglist.append(currentpiece)
                    currentpiece.shape('redKing.gif')

            elif currentpiece in self.blacklist:
                if currentpiece.ycor()>300:
                    self.kinglist.append(currentpiece)
                    currentpiece.shape('blackKing.gif')

            #these next statements move a piece off the board when it has been skipped
            #red piece moved
            if currentpiece in self.redlist:  
                #if the player skipped down and left
                if self.moverclicked==self.DL:
                    #check which piece it is
                    for i in self.blacklist:
                        if ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                            #move it off the board
                            i.goto(-450,0)
                            i.hideturtle()
                            return
                #DR
                if self.moverclicked==self.DR:
                    for i in self.blacklist:
                        if ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                            i.goto(-450,0)
                            i.hideturtle()
                            return
            #black piece moved
            if currentpiece in self.blacklist:
                #UR
                if self.moverclicked==self.UR:
                    for i in self.redlist:
                        if ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                            i.goto(450,0)
                            i.hideturtle()
                            return
                #UL
                if self.moverclicked==self.UL:
                    for i in self.redlist:
                        if ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                            i.goto(450,0)
                            i.hideturtle()
                            return

            #king piece moved
            # it is the above statements but the lists are reversed so that black kings can skip down and red kings can skip up
            if (currentpiece in self.kinglist):
                #DL
                if self.moverclicked==self.DL:
                    for i in self.redlist:
                        if ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                            i.goto(-450,0)
                            i.hideturtle()
                            return
                #DR
                if self.moverclicked==self.DR:
                    for i in self.redlist:
                        if ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                            i.goto(-450,0)
                            i.hideturtle()
                            return
                #UR
                if self.moverclicked==self.UR:
                    for i in self.blacklist:
                        if ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                            i.goto(450,0)
                            i.hideturtle()
                            return
                #UL
                if self.moverclicked==self.UL:
                    for i in self.blacklist:
                        if ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                            i.goto(450,0)
                            i.hideturtle()
                            return
        #hiding the movers
        for i in self.movers:
            i.hideturtle()

        #the following code is literally just to find where to place the movers, which act as a check for if a move is valid
        #the different types of pieces are blocked in sections by ### to make it easier to look at

        ############################################

        #the king piece movement is simply a combination of the red and black movements explained below
        if currentpiece in self.kinglist:
            DLmove=[]
            DRmove=[]
            ULmove=[]
            URmove=[]

            for i in self.piecelist:
                if not ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                    DLmove.append(True)
                elif ((currentpiece in self.redlist) and (i in self.blacklist)) or ((currentpiece in self.blacklist) and (i in self.redlist)):
                    DLmove.append('skip')
                else:
                    DLmove.append(False)
                if not ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                    DRmove.append(True)
                elif ((currentpiece in self.redlist) and (i in self.blacklist)) or ((currentpiece in self.blacklist) and (i in self.redlist)):
                    DRmove.append('skip')
                else:
                    DRmove.append(False)
                if not ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                    ULmove.append(True)
                elif ((currentpiece in self.redlist) and (i in self.blacklist)) or ((currentpiece in self.blacklist) and (i in self.redlist)):
                    ULmove.append('skip')
                else:
                    ULmove.append(False)
                if not ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                    URmove.append(True)
                elif ((currentpiece in self.redlist) and (i in self.blacklist)) or ((currentpiece in self.blacklist) and (i in self.redlist)):
                    URmove.append('skip')
                else:
                    URmove.append(False)

            if (False not in DLmove) and ('skip' not in DLmove):
                self.DL.showturtle()
                self.DL.goto(currentpiece.xcor()-100,currentpiece.ycor()-100)
                self.DL.onclick(move)
            elif ('skip' in DLmove):
                for i in self.piecelist:
                    if not ((currentpiece.xcor()-190>i.xcor()>currentpiece.xcor()-210) and (currentpiece.ycor()-190>i.ycor()>currentpiece.ycor()-210)):
                        self.DL.showturtle()
                        self.DL.goto(currentpiece.xcor()-200,currentpiece.ycor()-200)
                        self.DL.onclick(move)
                    else:
                        self.DL.hideturtle()
                        break

            if (False not in DRmove) and ('skip' not in DRmove):
                self.DR.showturtle()
                self.DR.goto(currentpiece.xcor()+100,currentpiece.ycor()-100)
                self.DR.onclick(move)
            elif ('skip' in DRmove):
                for i in self.piecelist:
                    if not ((currentpiece.xcor()+190<i.xcor()<currentpiece.xcor()+210) and (currentpiece.ycor()-190>i.ycor()>currentpiece.ycor()-210)):
                        self.DR.showturtle()
                        self.DR.goto(currentpiece.xcor()+200,currentpiece.ycor()-200)
                        self.DR.onclick(move)
                    else:
                        self.DR.hideturtle()
                        break
                
            if (False not in ULmove) and ('skip' not in ULmove):
                self.UL.showturtle()
                self.UL.goto(currentpiece.xcor()-100,currentpiece.ycor()+100)
                self.UL.onclick(move)
            elif ('skip' in ULmove):
                for i in self.piecelist:
                    if not ((currentpiece.xcor()-190>i.xcor()>currentpiece.xcor()-210) and (currentpiece.ycor()+190<i.ycor()<currentpiece.ycor()+210)):
                        self.UL.showturtle()
                        self.UL.goto(currentpiece.xcor()-200,currentpiece.ycor()+200)
                        self.UL.onclick(move) 
                    else:
                        self.UL.hideturtle()
                        break
                 
            if (False not in URmove) and ('skip' not in URmove):
                self.UR.showturtle()
                self.UR.goto(currentpiece.xcor()+100,currentpiece.ycor()+100)
                self.UR.onclick(move)
            elif ('skip' in URmove):
                for i in self.piecelist:
                    if not ((currentpiece.xcor()+190<i.xcor()<currentpiece.xcor()+210) and (currentpiece.ycor()+190<i.ycor()<currentpiece.ycor()+210)):
                        self.UR.showturtle()
                        self.UR.goto(currentpiece.xcor()+200,currentpiece.ycor()+200)
                        self.UR.onclick(move)
                    else:
                        self.UR.hideturtle()
                        break

        ###########################################################

        #if it is a red piece that was moved
        elif currentpiece in self.redlist:
            #i initially used lists for checking to see if a move was valid for debugging purposes but chose to keep it because it worked well
            #why fix it if it isnt broken
            DLmove=[]
            DRmove=[]
            #for every piece on the board
            for i in self.piecelist:
                #if there isnt a piece in the way, append a True value
                if not ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                    DLmove.append(True)
                #or if there is a black piece in the way, append a skip value
                elif i in self.blacklist:
                    DLmove.append('skip')
                #if neither, that direction of movement is false
                else:
                    DLmove.append(False)
                #same as above but in a different direction
                if not ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()-90>i.ycor()>currentpiece.ycor()-110)):
                    DRmove.append(True)
                elif i in self.blacklist:
                    DRmove.append('skip')
                else:
                    DRmove.append(False)

            #if all move values in the list are true, place the mover and the player may move there
            if (False not in DLmove) and ('skip' not in DLmove):
                self.DL.showturtle()
                self.DL.goto(currentpiece.xcor()-100,currentpiece.ycor()-100)
                self.DL.onclick(move)
            #but if there is a skip value
            elif ('skip' in DLmove):
                #for every piece
                for i in self.piecelist:
                    #if there is not a piece after the desired skippable piece, place the mover
                    if not ((currentpiece.xcor()-190>i.xcor()>currentpiece.xcor()-210) and (currentpiece.ycor()-190>i.ycor()>currentpiece.ycor()-210)):
                        self.DL.showturtle()
                        self.DL.goto(currentpiece.xcor()-200,currentpiece.ycor()-200)
                        self.DL.onclick(move)
                    #if there is, hide the mover and break the loop
                    else:
                        self.DL.hideturtle()
                        break

            #same as above but a different direction
            if (False not in DRmove) and ('skip' not in DRmove):
                self.DR.showturtle()
                self.DR.goto(currentpiece.xcor()+100,currentpiece.ycor()-100)
                self.DR.onclick(move)
            elif ('skip' in DRmove):
                for i in self.piecelist:
                    if not ((currentpiece.xcor()+190<i.xcor()<currentpiece.xcor()+210) and (currentpiece.ycor()-190>i.ycor()>currentpiece.ycor()-210)):
                        self.DR.showturtle()
                        self.DR.goto(currentpiece.xcor()+200,currentpiece.ycor()-200)
                        self.DR.onclick(move)
                    else:
                        self.DR.hideturtle()
                        break

        ########################################################

        #black piece movement is simply the same as red piece but the coordinates are flipped since black pieces move up
        elif currentpiece in self.blacklist:
            ULmove=[]
            URmove=[]
            for i in self.piecelist:
                if not ((currentpiece.xcor()-90>i.xcor()>currentpiece.xcor()-110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                    ULmove.append(True)
                elif i in self.redlist:
                    ULmove.append('skip')
                else:
                    ULmove.append(False)
                if not ((currentpiece.xcor()+90<i.xcor()<currentpiece.xcor()+110) and (currentpiece.ycor()+90<i.ycor()<currentpiece.ycor()+110)):
                    URmove.append(True)
                elif i in self.redlist:
                    URmove.append('skip')
                else:
                    URmove.append(False)
            if (False not in ULmove) and ('skip' not in ULmove):
                self.UL.showturtle()
                self.UL.goto(currentpiece.xcor()-100,currentpiece.ycor()+100)
                self.UL.onclick(move)
            elif ('skip' in ULmove):
                for i in self.piecelist:
                    if not ((currentpiece.xcor()-190>i.xcor()>currentpiece.xcor()-210) and (currentpiece.ycor()+190<i.ycor()<currentpiece.ycor()+210)):
                        self.UL.showturtle()
                        self.UL.goto(currentpiece.xcor()-200,currentpiece.ycor()+200)
                        self.UL.onclick(move) 
                    else:
                        self.UL.hideturtle()
                        break
                 
            if (False not in URmove) and ('skip' not in URmove):
                self.UR.showturtle()
                self.UR.goto(currentpiece.xcor()+100,currentpiece.ycor()+100)
                self.UR.onclick(move)
            elif ('skip' in URmove):
                for i in self.piecelist:
                    if not ((currentpiece.xcor()+190<i.xcor()<currentpiece.xcor()+210) and (currentpiece.ycor()+190<i.ycor()<currentpiece.ycor()+210)):
                        self.UR.showturtle()
                        self.UR.goto(currentpiece.xcor()+200,currentpiece.ycor()+200)
                        self.UR.onclick(move)
                    else:
                        self.UR.hideturtle()
                        break
