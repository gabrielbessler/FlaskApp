from Piece import Piece


class Knight (Piece):

    def __init__(self, color):
        '''
        Creates a Knight object of a given color with the allowed moveset
        and value 3
        '''
        self.knightMoves = [[-1,  1, -1,  1, -1],
                            [1, -1, -1, -1,  1],
                            [-1, -1,  0, -1, -1],
                            [1, -1, -1, -1,  1],
                            [-1,  1, -1,  1, -1]]
        self.setName("Knight")
        self.setColor(color)
        self.upAllowed = True
        self.setMoves(moveSet=self.knightMoves)
        self.setValue(3)

    def __str__(self):
        '''
        Returns a string representation of a knight of a given color
        '''
        return f"{self.getName()}({self.getColor()})"
