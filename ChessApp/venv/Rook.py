from Piece import Piece

class Rook (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Rook")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(leftAllowed = True, rightAllowed = True, upAllowed = True, downAllowed = True)
        self.setValue(5)

    def __str__(self):
        return f"{self.getName()}({self.getColor()})"
