from flask import Flask, request, redirect
app = Flask(__name__)

# 1 for ongoing games
# 0 otherwise
games = [0] * 10

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

@app.route('/game/<int:game_num>')
def get_game(game_num):
    '''
    '''
    if games[game_num] <= 2:
        games[game_num] += 1
    return f'This is game number {game_num}'

