from Piece import Piece

class Bishop (Piece):

    def __init__(self, color):
        '''
        Initializes the bishop object
        '''
        self.setName("Bishop")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves()
        self.setValue(3)

    def __str__(self):
        return f"{self.getName()}({self.getColor()})"

    def setMoves(self):
        '''
        Updates the movement variables for the bishop
        '''
        self.diag_right = True
        self.diag_left = True
