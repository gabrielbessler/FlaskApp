from Piece import Piece

class Queen (Piece):

    def __init__(self, color):
        '''
        '''
        self.setName("Queen")
        self.setColor(color)
        self.upAllowed = True

