from Piece import Piece

class Rook (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Rook")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves()
        self.setValue(5)

    def __str__(self):
        return f'{self.getName()}({self.getColor()})'

    def setMoves(self):
        '''
        Updates the movement variables for the pawn
        '''
        self.left_allowed = True
        self.right_allowed = True
        self.up_allowed = True
        self.down_allowed = True
