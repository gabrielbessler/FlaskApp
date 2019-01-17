from Piece import Piece


class Rook(Piece):

    def __init__(self, color):
        '''
        Creates a rook object of a given color with the allowed
        moveset and value 5
        '''
        self.setName("Rook")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(leftAllowed=True, rightAllowed=True, upAllowed=True, downAllowed=True)
        self.setValue(5)

    def __str__(self):
        '''
        Returns the String representation of the Rook
        '''
        return f"{self.getName()}({self.getColor()})"
