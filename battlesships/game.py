
def new_game():
    #print 'game.new_game start'
    print '<<<.\* Welcome to BATTLESHIPS!!! */.>>>'
    start = raw_input('Do you want to play? Y/N')
    if start.upper() == 'Y':
        'Let\'s start!'
    else:
        return


def initialize_game_stats():
    bombs = 25
    game_playing = True
    ship_squares_found = 0
    return bombs, game_playing, ship_squares_found


def check_game_status(ship_squares_found,game_playing, bombs):
    if ship_squares_found == 15:
        message = "You won!!!"
        game_playing = False
    else: #ships not found
        if bombs == 0:
            message = "You lost!!!"
            game_playing = False
        else: # bombs left
            game_playing = True
            message = ""
    print message
    return game_playing


def end_turn(board,i,j,bombs,ship_squares_found):
        bombs = bombs - 1
        board[i][j].shown = True
        if board[i][j].ship == True:
            print 'you hit a ship!'
            ship_squares_found = ship_squares_found + 1
        else:
            print 'you missed!'
        print 'you have ', bombs, ' bombs left'
        return board, bombs, ship_squares_found
