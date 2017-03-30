
class Square(object):
    def __init__(self):
        self.empty = True
        self.player = ''
    #add method to check empty one var

class Board(object):
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                            [0, 3, 6], [1, 4, 7], [2, 5, 8],
                            [0, 4, 8], [2, 4, 6]]

    def __init__(self):
        self.squares = [Square() for i in range(9)]

    #Marks a square taken by a player
    def mark_square(self, square_index, name):
        print 'marking square ', square_index, 'for player', name
        self.squares[square_index].empty = False
        self.squares[square_index].player = name

    #Checks if there are still empty squares left
    def check_if_board_full(self):
        game_playing = False
        for square in self.squares:
            if square.empty == True:
                game_playing = True
        if game_playing == False:
            print 'Game over! Noone won!'
        return game_playing
