"""
Problems to solve:
convert input does not recognize 10
get input doesnt have unrecognizable input plan
"""


import boardsetup
import display
import game
import inputter


board = boardsetup.get_ready_to_use_board()
bombs, game_playing, ship_squares_found = game.initialize_game_stats()
print bombs, game_playing, ship_squares_found
game.new_game()

while game_playing == True:
    display.display_board(board)

    user_input = inputter.get_input()

    if user_input == 'Q':
        break
    else:
        processed_input = inputter.process_input(user_input)
        print processed_input
        if processed_input[0] == True:
            i,j = processed_input[1], processed_input[2]
            board, bombs, ship_squares_found = game.end_turn(board,i,j,bombs,ship_squares_found)

    print '\n'

    game_playing = game.check_game_status(ship_squares_found,game_playing,bombs)
