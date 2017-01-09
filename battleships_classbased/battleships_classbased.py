"""
Improvements:
- remove game class
things to do with board go to board, things to do with driver go to driver
- make the board represented with a numpy array? and consistent - visualization
and keeping track by same way, see this:
http://thelivingpearl.com/2014/01/29/the-game-of-tic-tac-toe-in-python/
- complete the random ship placer

-then make a modulated one that is not in classes?
"""


class Driver(object):
    def __init__(self):
        pass

    def start_up(self):
        print '<<<.\* Welcome to BATTLESHIPS!!! */.>>>'
        start = raw_input('Do you want to play? Y/N')
        if start.upper() == 'Y':
            self.new_game()
        else:
            return

    def new_game(self):
        print "Let's play!"
        print "You have ", game.bombs, " bombs to find and hit all the ships: "
        print " <> \n <O> \n <OO> \n <OOO> \n <OOOO>"
        print "Once hit, ship segments are represented by S's on the grid, regardless of direction"
        print "Press 'Q' to end the game \n"

        game.new_board()
        game.new_game()


    def display_board(self):
        squares = ['0'] + game.squares_status
        alphabet = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        board = [' '] + [str(i) for i in range(1, game.board.size+1)] + ['\n \n']
        for number in range(1, game.board.size+1):
            start = (number*game.board.size) - (game.board.size-1)
            end = number*game.board.size+1
            board = board + [alphabet[number]] + squares[start:end] + ['\n \n']
        for item in board:
            print '  ', item,


    def display_stats(self):
        bombs = game.bombs
        print 'You have ', bombs, ' bombs left '

    def display_message(self, message):
        print message

    def get_input(self):
        print 'Choose a square!'
        user_input = raw_input('-->').upper()

        alphabet = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        #convert = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        convert = [] #MAKE THIS NICER!!!!!
        for number in range(1, game.board.size+1):
            for each in range(1, game.board.size+1):
                convert.append(alphabet[number] + str(each))

        if user_input == 'Q':
            return
        elif user_input in convert:
            guess = convert.index(user_input)
            game.end_turn(guess)
        else:
            print 'Try again! Aim for the grid'
            self.get_input()


class Game(object):

    def __init__(self):
        #print 'game object initializing'
        self.bombs = 15
        self.game_playing = True
        self.ships_found = False
        #print 'game object initialized'

    def new_game(self):
        #print 'game.new_game start'
        self.set_ships()
        self.new_turn()
        #print 'end'

    def new_board(self):
        self.board = Board()
        self.squares_status = ['?' for i in self.board.squares_ship]
        #self.set_ships()
        #print 'board made'

    def set_ships(self):
        #create 2d list


        #choose down or right
        #find options
        #choose randomly

        self.board.squares[1].ship = True
        self.board.squares[5].ship = True
        self.board.squares[8].ship = True
        #print 'ships set'

    def check_status(self):
        if self.ships_found == True:
            driver.display_message("You won!!!")
            self.game_playing = False
        else: #ships not found
            if bombs == 0:
                driver.display_message("You lost!!!")
                self.game_playing = False
            else: # bombs left
                self.game_playing = True

    def get_squares_status(self):
        i = 0
        while i < len(self.squares_status):
            #if shown true
            if self.board.squares_shown[i] == True:
                #if ship True
                if self.board.squares_ship[i] == True:
                    self.squares_status[i] = 'S'
                #else if ship False
                else:
                    self.squares_status[i] = '/'
            #else shown not true
            else:
                self.squares_status[i] = '?'
            i += 1


    def new_turn(self):
        #print 'new turn start'
        driver.display_board()
        driver.display_stats()
        driver.get_input()
        #print 'new turn end'

    def end_turn(self, guess):
        #print 'you guessed ', guess
        self.bombs = self.bombs - 1
        self.board.squares[guess].shown = True
        if self.board.squares[guess].ship == True:
            driver.display_message('you hit a ship!')
        else:
            driver.display_message('you missed!')
        self.board.check_squares()
        self.get_squares_status()
        self.new_turn()

class Board(object):
    size = 10

    def __init__(self):
        self.squares = [Square(i) for i in range(1,(self.size*self.size+1),1)]
        self.squares_ship = [False for each in self.squares]
        self.squares_shown = [False for each in self.squares]

    def check_squares(self):
        for each in self.squares:
            the_id = each.id
            is_ship = each.ship
            is_shown = each.shown

            self.squares_ship[the_id-1] = is_ship
            self.squares_shown[the_id-1] = is_shown


class Square(object):
    def __init__(self, id):
        self.id = id
        self.ship = False
        self.shown = False

driver = Driver()
game = Game()
driver.start_up()
