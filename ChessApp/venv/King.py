from Piece import Piece

class King (Piece):

    def __init__(self, color):
        '''
        '''
        self.kingMoves = [[1,1,1], \
                         [1,0,1], \
                         [1,1,1]]
        self.setName("King")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(moveSet = self.kingMoves)
        self.setValue(10000)

    def __str__(self):
        return f"{self.getName()}({self.getColor()})"
