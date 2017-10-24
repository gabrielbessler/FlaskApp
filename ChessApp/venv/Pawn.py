from Piece import Piece

class Pawn (Piece):

    def __init__(self, color):
        '''
        Creates a Queen object of a given color with the allowed moveset and value 1
        '''
        self.setName("Pawn")
        self.setColor(color)
        self.upAllowed = True
        if color == 0:
            self.setMoves(moveSet = [[-1,3,-1],[2,1,2],[-1,0,-1]])
        else:
            self.setMoves(moveSet = [[-1,0,-1],[2,1,2],[-1,3,-1]])
        self.setValue(1)
        self.hasMoved = False

    def __str__(self):
        '''
        Returns a string representation of the pawn of a given color
        '''
        return f"{self.getName()}({self.getColor()})"
