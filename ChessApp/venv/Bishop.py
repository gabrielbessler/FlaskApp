from Piece import Piece

class Bishop (Piece):

    def __init__(self, color):
        '''
        Creates a Bishop object of a given color with the allowed moveset and value 3
        '''
        self.setName("Bishop")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(diagRight = True, diagLeft = True)
        self.setValue(3)

    def __str__(self):
        '''
        Returns a string representation of a King of a given color
        '''
        return f"{self.getName()}({self.getColor()})"
