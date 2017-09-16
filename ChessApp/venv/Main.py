from flask import Flask, request, redirect, abort
from Game import Game
app = Flask(__name__)

# 1 for ongoing games
# 0 otherwise
games = [0] * 10
store_games = {}

@app.route('/', methods=["POST", "GET"])
def hello_word():
    if request.method == "POST":
        game_value = get_next_game()
        if game_value == -1:
            return "Games in progress...please wait..."
        else:
            return redirect("game\\" + str(get_next_game()))
    display = ""
    for game_index, game_on in enumerate(games):
        display += f"Game {game_index+1}, Available: {bool(not game_on)} <br>"
    return display + "<form method='post'> <button type='submit'> Connect to Game </button> </form> "

def get_next_game():
    '''
    Loops through the list of ongoing games and finds the next game available
    '''
    for game_id, game_value in enumerate(games):
        if game_value == 0:
            return game_id
    # consider aborting here
    return -1

@app.route('/game/<int:game_num>', methods=["POST", "GET"])
def get_game(game_num):
    '''
    '''
    if request.method == "POST":
        try:
            var = request.form['test']
            return store_games[game_num].make_move(str(var))

        except (KeyError):
            abort(404)
    elif request.method == "GET":
        if games[game_num] <= 2:
            games[game_num] += 1
            if games[game_num] == 2:
                new_game = Game()
                store_games[game_num] = new_game
                return str(store_games[game_num]) + \
            "<form method='POST'> \
                    <input type='text' value='1234' name='test'> </input> \
                    <button type='submit'> Make Move! </button> \
            </form>"
            pass
        return f'This is game number {game_num}'