from Piece import Piece

class Pawn (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Pawn")
        self.setColor(color)
        self.upAllowed = True
    
    def __str__(self):
        return 'Pawn'
