
import interface
import board
import player

### DECLARE VARIBLES ###
game_playing = True
turn_count = 0
board = board.Board()

playerX = player.Player('X', False)
playerO = player.Player('O', True)

#Display board to start:
interface.display_board(board)

### GAME LOOP ###
while game_playing:

    # determine whose turn it is
    if turn_count % 2 == 0:
        current_player = playerX
    else:
        current_player = playerO

    if not current_player.computer: # == False:
        #USER TURN STARTS HERE
        #start turn / tell which player
        current_player.start_my_turn()

        #get user input
        user_input = interface.get_input()

        #end game if user exits
        if user_input == 'Q':
            game_playing = False
            break

        #get the index from the input
        result = interface.process_input(user_input)
    else:
        result = current_player.get_computer_play(board)

    #check if input is valid and square is empty
    if result[0] and board.squares[result[1]].empty:
        board.mark_square(result[1], current_player.name)
        turn_count = turn_count + 1
    else:
        print 'oops try again'


    # display board
    interface.display_board(board)

    #check if game is over/ won
    game_playing = board.check_if_board_full()
    game_playing = playerX.check_if_winner(board, game_playing)
    game_playing = playerO.check_if_winner(board, game_playing)
