from Board import Board

class Game():

    def __init__(self):
        '''

        '''
        self.board = Board()
        self.curr_turn = 0

    def __repr__(self):
        '''

        '''
        return "This is the representation of the board"

    def __str__(self):
        return "THIS IS A GAME"

    def make_move(self, move):
        '''
        '''
        self.board(self, (move[0], move[1]), (move[2], move[3]))