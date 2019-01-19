'''
Contains all of the information for an instance of the game.
'''

from pieces import Rook, Knight, Bishop, Queen, Pawn, King

class Board:
    '''
    Stores boardstate of game.
    '''
    def __init__(self):
        '''
        Sets up all of the pieces that are initially on the board
        when the game starts
        '''
        self.board = []
        self.set_initial_state()

    def get_raw(self):
        ''' Get the raw data from the board to send to the user
        '''
        string_board = '['
        for x_pos in range(8):
            string_board += "["
            for y_pos in range(8):
                string_board += '"' + str(self.board[x_pos][y_pos]) + '"'
                if y_pos != 7:
                    string_board += ','
            string_board += "]"
            if x_pos != 7:
                string_board += ","
        string_board += ']'
        return string_board

    def __str__(self):
        '''
        Returns a string representation of the current board
        Used for debugging
        '''
        string_board = ''
        for x_pos in range(8):
            for y_pos in range(8):
                string_board += str(self.board[x_pos][y_pos]) + ' '
            string_board += '<br>'
        return string_board

    def get_moveset_moves(self, coord, move_set, piece, turn):
        ''' Get all of the possible moves from a moveset '''
        center_x, center_y = 0, 0
        moves = []
        coord_x = int(coord[0])
        coord_y = int(coord[1])

        for rownum, row in enumerate(move_set):
            for colnum in range(len(row)):
                if move_set[rownum][colnum] == 0:
                    center_x, center_y = rownum, colnum

        for rownum, row in enumerate(move_set):
            for colnum in range(len(row)):
                if move_set[rownum][colnum] == 1:
                    moves += [[colnum-center_x+coord_x,
                               rownum-center_y+coord_y]]
                elif move_set[rownum][colnum] == 3:
                    if not piece.hasMoved:
                        moves += [[colnum-center_x+coord_x,
                                   rownum-center_y+coord_y]]
                elif move_set[rownum][colnum] == 2:
                    piece2 = self.board[colnum-center_x+coord_x][rownum-center_y+coord_y]
                    if piece2 != 0 and piece2.get_color() != int(turn):
                        moves += [[colnum-center_x+coord_x,
                                   rownum-center_y+coord_y]]

        return self.check_pieces(moves, turn)

    def get_move(self, coord, turn=-1):
        '''
        Gets all of the available squares that the piece at the given input
        coordinate can move to.
        '''
        # How we store the squares the piece can move to
        allowed_squares = []
        # First, we get the piece on the current board
        piece = self.board[int(coord[0])][int(coord[1])]

        # Make sure the player is not trying to move a piece of the wrong color
        if turn != -1 and piece.get_color() != turn:
            return []

        # Obtain the moveset for the given piece
        allowed_moves = piece.get_allowed_moves()
        allowed_squares += self.get_moveset_moves(coord, allowed_moves[-1], piece, turn)

        coord_x = int(coord[0])
        coord_y = int(coord[1])

        # Up Allowed
        if allowed_moves[0]:
            for x_pos in range(coord_y+1, 8):
                if x_pos != coord_y:
                    piece = self.board[coord_x][x_pos]
        # Left Allowed
        if allowed_moves[1]:
            allowed_squares += [[x_pos, coord_y] for x_pos in range(8) if x_pos != coord_x]
        # Right Allowed
        if allowed_moves[2]:
            pass
        # Down Allowed
        if allowed_moves[3]:
            for x_pos in range(0, coord_y):
                if x_pos != coord_y:
                    allowed_squares.append([coord_x, x_pos])
        # Diag Left
        if allowed_moves[4]:
            allowed_squares += [[coord_x-1-x_pos, coord_y-1-x_pos] for x_pos in
                                range(min(coord_x, coord_y))]
            allowed_squares += [[coord_x+1+x_pos, coord_y+1+x_pos] for x_pos in
                                range(min(7-coord_x, 7-coord_y))]
        # Diag Right
        if allowed_moves[5]:
            allowed_squares += [[coord_x-1-x_pos, coord_y+1+x_pos] for x_pos in range(coord_x)]
            allowed_squares += [[coord_x+1+x_pos, coord_y-1-x_pos] for x_pos in
                                range(7-coord_x)]

        return self.check_pieces(allowed_squares, turn)

    def is_piece(self, coord):
        '''
        TODO: use this
        '''
        piece = self.board[coord[0]][coord[1]]
        if piece == 0:
            return False
        return True

    def check_pieces(self, coords, turn):
        '''
        Given a set of available moves, removes all of the pieces that are of
        the same color as your piece
        '''
        out_l = []
        for coord in coords:
            piece = self.board[coord[0]][coord[1]]
            if piece == 0:
                out_l.append(coord)
            else:
                if piece.getColor() != int(turn):
                    out_l.append(coord)
                else:
                    pass

        return out_l

    def move(self, current_square, next_square, turn):
        '''
        Takes in two locations. Moves piece from current
        square to next Square and replaces the piece with a zero
        '''
        piece = self.board[current_square[0]][current_square[1]]
        target = self.board[next_square[0]][next_square[1]]

        # if we try to move an empty square or move a piece no squares,
        #  or on top of a piece of our own color
        if piece == 0:
            raise ValueError("No Piece Selected")
        if current_square == next_square:
            raise ValueError("Cannot Move to Same Position")
        else:
            if target != 0:
                if target.getColor() == piece.getColor():
                    raise ValueError("Cannot Take a Piece of Same Color")
            if piece.getColor() != turn:
                raise ValueError("Cannot move your opponent's piece")
            # check if given a piece and a different starting/ending square,
            # it is a valid move
            if self.is_valid_move(piece, current_square, next_square):
                self.board[current_square[0]][current_square[1]] = 0
                self.board[next_square[0]][next_square[1]] = piece
                if hasattr(piece, 'hasMoved'):
                    piece.hasMoved = True
                return f"Made Move: {current_square, next_square} \
                for piece {piece} <br>"

            raise ValueError("Move Not in Moveset")

    def check_for_mate(self):
        '''
        Temporary
        '''
        print(self)
        return True

    # TODO
    # def check_for_mate(self):
    #    ''' Looks at the current board state and returns True if there
    #    is a checkmate
    #    '''
    #
    #    # TODO: First, check if the king is in check
    #    # If the king is in check, check if it has any available moves
    #
    #    # Check if the king is on the board. If not, it is mate
    #    king_count = 0
    #    for row in self.board:
    #        for col in row:
    #            if 1 == 1:
    #                king_count += 1
    #    if king_count == 2:
    #        return True
    #
    #    return False

    def is_valid_move(self, piece, current_square, next_square):
        ''' temporary method for testing '''
        print(piece)
        print(current_square)
        print(next_square)
        if piece == 123:
            self.is_valid_move(piece, current_square, next_square)
    # def is_valid_move(self, piece, current_square, next_square):
    #    '''
    #    TODO
    #    '''
    #    move_l = self.get_move(current_square)
    #    if next_square in move_l:
    #        return True
    #    return False
    #
    #    # then, we check the difference between the next_square and
    #    # current_square
    #    # x_diff = next_square[0] - current_square[0]
    #    # y_diff = next_square[1] - current_square[1]

    # TODO
    # def check_winner(self):
    #    '''
    #    Checks winner by determining if there are two kings on the
    #    board
    #    '''
    #    king_list = []
    #    for col in self.board:
    #        for row in self.board:
    #            if str(row) == "King":
    #                king_list.append(row)
    #    if len(king_list) == 1:
    #        return king_list[0].getColor()

    def get_board(self):
        '''
        Returns the current board
        '''
        return self.board

    def set_initial_state(self):
        '''
        Creates and initializes the board
        '''
        self.board = [[Rook(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Rook(0)],
                      [Knight(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Knight(0)],
                      [Bishop(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Bishop(0)],
                      [Queen(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Queen(0)],
                      [King(1), Pawn(1), 0, 0, 0, 0, Pawn(0), King(0)],
                      [Bishop(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Bishop(0)],
                      [Knight(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Knight(0)],
                      [Rook(1), Pawn(1), 0, 0, 0, 0, Pawn(0), Rook(0)]]

    def get_total_score(self):
        '''
        Count the total score for black and white and returns
        [WhiteScore, BlackScore]
        '''
        total_white_score = 0
        total_black_score = 0
        for i in self.board:
            for j in i:
                if j != 0:
                    if j.get_color() == 0:
                        total_white_score += j.get_value()
                    elif j.get_color() == 1:
                        total_black_score += j.get_value()

        return [total_white_score, total_black_score]
