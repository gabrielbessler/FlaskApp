from Piece import Piece

class King (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("King")
        self.setColor(color)
        self.upAllowed = True
    
    def __str__(self):
        return 'King'
