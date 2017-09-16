from Piece import Piece

class Knight (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Knight")
        self.setColor(color)
        self.upAllowed = True
    
    def __str__ (self):
        return "Knight"
