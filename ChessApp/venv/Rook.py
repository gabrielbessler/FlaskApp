from Piece import Piece

class Rook (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Rook")
        self.setColor(color)
        self.upAllowed = True

