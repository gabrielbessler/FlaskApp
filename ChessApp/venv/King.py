from Piece import Piece


class King (Piece):

    def __init__(self, color):
        '''
        Creates a King object of a given color with the allowed moveset
        and value 0
        '''
        self.kingMoves = [[1, 1, 1],
                          [1, 0, 1],
                          [1, 1, 1]]
        self.setName("King")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(moveSet=self.kingMoves)
        self.setValue(0)

    def __str__(self):
        '''
        Returns a string representation of a King of a given color
        '''
        return f"{self.getName()}({self.getColor()})"
