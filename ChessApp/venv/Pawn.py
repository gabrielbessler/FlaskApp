from Piece import Piece

class Pawn (Piece):

    def __init__(self, color):
        '''
        Creates a Queen object of a given color with the allowed moveset and value 1
        '''
        self.setName("Pawn")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(moveSet = [[2,1,2],[-1,0,-1]])
        self.setValue(1)

    def __str__(self):
        '''
        Returns a string representation of the pawn of a given color
        '''
        return f"{self.getName()}({self.getColor()})"
