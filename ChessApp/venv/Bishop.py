from Piece import Piece

class Bishop (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Bishop")
        self.setColor(color)
        self.upAllowed = True
    
    def __str__(self):
        return "Bishop"
