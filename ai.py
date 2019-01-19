''' Using a mini-max algorithm with alpha-beta pruning to find best moves'''
class AI:
    ''' AI to Play Chess Game '''
    def __init__(self, color=5, move_time=5):
        ''' Creates the new AI object that will be stored in the game
        '''
        # One mode limits the amount of time the engine can spend on
        # a single move, while the other limits the depth it can search
        self.mode = 'move_time'
        self.move_time = move_time
        self.target_depth = 10
        # Store a set of opening lines in a dictionary that the AI
        # can use
        # The keys are board data and the values are the best move
        self.openings = {}
        self.color = color
        self.evaluation_type = 1

    def get_next_move(self, board_data):
        ''' Given the data about the board, the AI will run a minimax
        algorithm to find the best move in a given amount of time
        '''
        # First, check if the current board state is in the openings
        # dictionary
        if board_data in self.openings:
            return self.openings[board_data]

        return "1234"

    def evaluate_board(self):
        ''' Gives a input board a score from 0-100
        '''
        # Simplest approach: if the board is winning for our opponent,
        # we return 0. If the board is winning for us, we return 100

        # More complex approach: take into account piece values
        if self.evaluation_type == 1:
            return 50

        return 0
