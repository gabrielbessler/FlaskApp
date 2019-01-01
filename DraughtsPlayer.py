from random import randint

# Rules: 
# Regular pieces can only move forwards
# But can jump in any direction
# If you can take a piece, you HAVE to take it 
# If there are multiple pieces to take, you have to take the one that 
#     will lead to the highest amount of captures for you 

# This means that we have to check all of the possible captures, 
# which means we need 

class Game():
    def __init__(self, playerOne, playerTwo):
        '''
        Create a new instance of the game
        '''
        self.board_width = 10
        self.board_height = 10
        self.board = [[0 for i in range(0, self.board_width)] for j in range(0, self.board_height)]
        self.player_one_pieces = []
        self.player_two_pieces = []
        self.initialBoardState()
        self.player_one = playerOne
        self.player_two = playerTwo

    def __str__(self):
        '''
        Print out a string representation of the current board state
        '''
        s = ""
        for y in range(0, self.board_width):
            for x in range(0, self.board_height):
                if (self.board[x][y] == 0):
                    s += str("__ ")
                else:
                    s += str(self.board[x][y]) + " "
            s += "\n"
        return s

    def initialBoardState(self):
        for x in range(0, self.board_width):
            for y in range(0, self.board_height):
                if (x + y) % 2 == 0:
                    if y < 4:
                        piece = Piece(0)
                        self.board[x][y] = piece
                        self.player_one_pieces.append(piece)
                    elif y > 5:
                        piece = Piece(1)
                        self.board[x][y] = piece
                        self.player_two_pieces.append(piece)

    def playGame(self):
        MAX_ITERATIONS = 1000
        iterations = 0
        while iterations < MAX_ITERATIONS:
            if (DEBUG):
                print(iterations)
                ans = input("Press enter to iterate. ")
                if ans == "b" or DEBUG_LEVEL == 1:
                    print(str(self))

            # Player One Move
            while True:
                moveSet = self.validMoves(0)
                moveOne = self.player_one.getMove()
                if moveOne in moveSet:
                    if (DEBUG):
                        print("Move One: " + str(moveOne))
                    self.makeMove(moveOne)
                    break
                if (self.gameOver()):
                    break

            # Player Two Move 
            while True:
                moveTwo = self.player_two.getMove()
                if self.isValid(moveTwo):
                    if (DEBUG):
                        print("Move Two: " + str(moveTwo))
                    self.makeMove(moveTwo)
                    break
                if self.gameOver():
                    break

            iterations += 1

        # Check who won 
        if len(self.player_one_pieces) == 0:
            print("Player Two Wins In " + str(iterations) + " iterations")
        else:
            print("Player One Wins In " + str(iterations) + " iterations")

    def gameOver(self):
        if len(self.player_one_pieces) == 0:
            return True
        if len(self.player_two_pieces) == 0:
            return True
        return False

    def isValid(self, move):
        # Make sure coordinates are actually in the board 
        for coord in move:
            if coord >= 10:
                return 0

        # Make sure we are moving diagonally
        diff_y = abs(move[3] - move[1])
        diff_x = abs(move[2] - move[0])
        if diff_x != diff_y:
            return 0

        # Make sure the destination is not a piece 
        if isinstance(self.board[move[2]][move[3]], Piece):
            return False

        # Check that we selected a piece 
        if isinstance(self.board[move[0]][move[1]], Piece):
            piece = self.board[move[0]][move[1]]
            pieceType = piece.getType()
            color = piece.getColor()

            if pieceType == 0: # pawn
                # Can only move one square or two squares if taking a piece 
                if diff_x == 1:
                    return True
                if diff_x == 2:
                    # If moving two, then the square in the middle has to be a piece 
                    x_add = int((move[2] - move[0]) / 2)
                    y_add = int((move[3] - move[1]) / 2)
                    if isinstance(self.board[move[0] + x_add][move[1] + y_add], Piece):
                        return True
                    return False
                return False
            elif pieceType == 1: #bishop
                return True

        return False

    def makeMove(self, move):
        # Move = [x1, y1, x2, y2]
        self.board[move[2]][move[3]] = self.board[move[0]][move[1]]

        diff_y = move[3] - move[1]
        diff_x = move[2] - move[0]
        diff_abs = abs(diff_x)

        self.board[move[0]][move[1]] = 0
        for i in range(1, diff_abs):

            target_x = move[0]
            target_y = move[1]
            if diff_y > 0:
                target_y += i
            else:
                target_y -= i

            if diff_x > 0:
                target_x += i
            else:
                target_x -= i
            piece = self.board[target_x][target_y]

            if isinstance(piece, Piece):
                if piece.getColor() == 0:
                    self.player_one_pieces.remove(piece)
                else:
                    self.player_two_pieces.remove(piece)
            self.board[target_x][target_y] = 0

class Piece():
    def __init__(self, color):
        self.color = color
        self.type = 0

    def __repr__(self):
        return "P" + str(self.color)

    def updateType(self):
        self.type = 1

    def getType(self):
        return self.type

    def getColor(self): 
        return self.color

class Player():
    def __init__(self): 
        pass 

    def getMove(self):
        return [randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)]

DEBUG = False
DEBUG_LEVEL = 1
def playGame(): 
    board = Game(Player(), Player())
    board.playGame()
   
input("Press enter to play. ")
playGame()
