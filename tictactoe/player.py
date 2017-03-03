import random

class Player(object):
    def __init__(self, name, comp):
        self.name = name
        ###### ~~~~~~~ add computer T/F attribute
        self.computer = comp

    #Starts this players turn
    def start_my_turn(self):
        print "It's player ", self.name, "'s turn"
        print "Choose a square"

    #Checks if this player won
    def check_if_winner(self, board, game_playing):
        my_squares = []
        for square in board.squares:
            if square.player == self.name:
                ind = board.squares.index(square)
                my_squares.append(ind)
        for combo in board.winning_combinations:
            got_combo = []
            for number in combo:
                if number in my_squares:
                    got_combo.append(True)
                else:
                    got_combo.append(False)
            if False not in got_combo:
                print 'GAME OVER!!! PLAYER ', self.name, ' WON!!!'
                game_playing = False
        return game_playing

###### ~~~~~~~ Method to get computer play
    def get_computer_play(self, board):
    ###### ~~~~~~~ 1) get empty squares
        empty_squares = []
        for (i, square) in enumerate(board.squares):
            if square.empty == True:
                empty_squares.append(i)
                print 'empty', i
    ###### ~~~~~~~ 2) get a random square from the empty squares
        random_index =random.choice(empty_squares)
        print random_index
        return (True, random_index)
