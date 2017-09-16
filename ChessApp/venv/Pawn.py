from Piece import Piece

class Pawn (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Pawn")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves()
        self.setValue(1)

    def __str__(self):
        return f"{self.getName()}({self.getColor()})"

    def setMoves(self):
        '''
        Updates the movement variables for the pawn
        '''
        self.move_set = [[2, 1, 2], \
                         [-1,0,-1]]