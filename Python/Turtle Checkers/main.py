import turtle as t 
import time
from Mode import PvP

#screen init
wn=t.Screen()
wn.setup(width=1050,height=850)
wn.title('Checkers')
#adding images in
wn.addshape('blackChecker.gif')
wn.addshape('redChecker.gif')
wn.addshape('redKing.gif')
wn.addshape('blackKing.gif')

writer=t.Turtle()
writer.speed(0)
writer.penup()
writer.hideturtle()

def drawMenu():
    t.clearscreen()
    writer.goto(0,300)
    writer.write('Checkers',align='center',font=('arial',72,'normal'))
    writer.goto(-500,200)
    writer.write('Player vs Player',align='left',font=('arial',20,'normal'))
    writer.goto(-500,100)
    writer.write('Player vs Computer',align='left',font=('arial',20,'normal'))
    writer.goto(-500,0)
    writer.write('Directions',align='left',font=('areal',20,'normal'))
    writer.goto(-500,-100)
    writer.write('Credits',align='left',font=('arial',20,'normal'))
    writer.goto(-500,-300)
    writer.write('press P for player vs player, press O for player vs computer, press I for directions, press C for credits, press Escape to return',align='left',font=('arial',12,'normal'))
    wn.onkey(pvp,"p")
    wn.onkey(pvc,"o")
    wn.onkey(directions,"i")
    wn.onkey(credit,"c")
    wn.onkey(drawMenu,"Escape")

def pvp():
    t.clearscreen()
    writer.goto(0,0)
    writer.write('Warning:\nPlease allow at least\n2 seconds before clicking\nthe white dots.',align='center',font=('arial',30,'normal'))
    time.sleep(5.0)
    t.clearscreen()
    PvP(wn).movelisten()
    wn.onkey(pvp,"p")
    wn.onkey(pvc,"o")
    wn.onkey(directions,"i")
    wn.onkey(credit,"c")
    wn.onkey(drawMenu,"Escape")

def pvc():
    t.clearscreen()
    writer.goto(0,300)
    writer.write('This mode is currently unavailable.',align='center',font=('arial',30,'normal'))
    wn.onkey(pvp,"p")
    wn.onkey(pvc,"o")
    wn.onkey(directions,"i")
    wn.onkey(credit,"c")
    wn.onkey(drawMenu,"Escape")

def credit():
    t.clearscreen()
    writer.goto(0,100)
    writer.write('Made by: Logan Fehn and Tyler Joest \n\nAssisted by: Mr.Bander, Gaege Smith, Eric Trice \n\nOutside sources: Stack Overflow, GeeksForGeeks',align='center',font=('arial',30,'normal'))
    wn.onkey(pvp,"p")
    wn.onkey(pvc,"o")
    wn.onkey(directions,"i")
    wn.onkey(credit,"c")
    wn.onkey(drawMenu,"Escape")

def directions():
    t.clearscreen()
    writer.goto(0,100)
    writer.write('Click a piece to select it.\nOnce selected, click the white dots to move it.\n\nIf you reach the other side,your piece turns into a king.\nThis allows you to move any direction.',align='center',font=('arial',30,'normal'))
    writer.goto(0,-150)
    writer.write('Attention:\nBy playing, you agree to the Honor System.\nYou, the player, are responsible for\nyour movements and scorekeeping.\nPlease play responsibly.',align='center',font=('arial',30,'normal'))
    wn.onkey(pvp,"p")
    wn.onkey(pvc,"o")
    wn.onkey(directions,"i")
    wn.onkey(credit,"c")
    wn.onkey(drawMenu,"Escape")

drawMenu()

wn.onkey(pvp,"p")
wn.onkey(pvc,"o")
wn.onkey(directions,"i")
wn.onkey(credit,"c")
wn.onkey(drawMenu,"Escape")

wn.listen()
wn.mainloop()