import turtle as t
from Board import Board
from Pieces import Pieces

class PvP:
    def __init__(self,wn):
        self.wn=wn
        #drawing main board
        #just stamps a bunch of squares
        Board(wn).drawBoard()
        #calling pieces class
        self.pieces=Pieces(wn)
        #calling placePieces method to place all pieces in inital spots
        self.piecelist,self.redlist,self.blacklist=self.pieces.placePieces()

    def movelisten(self):
        #when a piece is clicked it will call the moveCheck method
        def callMove(x,y):
            self.pieces.moveCheck(x,y)
        #detecting when each piece is clicked
        self.piecelist[0].onclick(callMove)
        self.piecelist[1].onclick(callMove)
        self.piecelist[2].onclick(callMove)
        self.piecelist[3].onclick(callMove)
        self.piecelist[4].onclick(callMove)
        self.piecelist[5].onclick(callMove)
        self.piecelist[6].onclick(callMove)
        self.piecelist[7].onclick(callMove)
        self.piecelist[8].onclick(callMove)
        self.piecelist[9].onclick(callMove)
        self.piecelist[10].onclick(callMove)
        self.piecelist[11].onclick(callMove)
        self.piecelist[12].onclick(callMove)
        self.piecelist[13].onclick(callMove)
        self.piecelist[14].onclick(callMove)
        self.piecelist[15].onclick(callMove)

