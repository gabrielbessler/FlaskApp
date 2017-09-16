import Piece

class Pawn (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Pawn")
        self.setColor(color)
        self.upAllowed = True

