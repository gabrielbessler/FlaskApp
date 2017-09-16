from flask import Flask, request, redirect
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
    return "Hello, World! <form method='post'> <button type='submit' value='Click Me!'> Test <//button> <//form> "

def get_next_game():
    ''' '''
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
        Game.make_move(request.form['move'])
        return request.form['move']
    elif request.method == "GET":
        if games[game_num] <= 2:
            games[game_num] += 1
            if games[game_num] == 2:
                new_game = Game()
                store_games[game_num] = new_game
                return str(store_games[game_num]) + \
            "<form method='POST'> \
                    <textarea name='move' rows='1' cols='4'/> \
                    <button type='submit' value='Enter Move'> \
            </form>"
            pass
        return f'This is game number {game_num}'