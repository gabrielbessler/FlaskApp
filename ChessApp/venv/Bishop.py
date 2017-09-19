from Piece import Piece

class Bishop (Piece):

    def __init__(self, color):
        '''
        Initializes the bishop object
        '''
        self.setName("Bishop")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(diagRight = True, diagLeft = True)
        self.setValue(3)

    def __str__(self):
        return f"{self.getName()}({self.getColor()})"
