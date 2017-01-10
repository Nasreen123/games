

class Square(object):
    def __init__(self, id):
        self.id = id
        self.ship = False
        self.shown = False
        self.buffer_or_taken = False

def set_board(length):
    #print 'set_board'
    board = []
    for i in range(length):
        board.append([Square( ((j)+(i*length)) ) for j in range(length)])
    return board

#this function check if the ship fits starting at a particular square
def does_ship_fit_here(board, starti, startj, direction, ship_size):
    #print 'does_ship_fit_here', len(board), starti, startj, direction, ship_size
    test = []
    if direction == 1: #ship will be placed horizontally, to the right
        i, j = 0, 1
    else: # ship will be placed vertically, going down
        j, i = 0, 1

    for number in range(ship_size):
        icoord = int(starti+(number*i)) #add number to start to move own/along
        jcoord = int(startj+(number*j)) #multiply by i or j (1 or 0) so in one direction only
        if icoord  < len(board) and jcoord < len(board): #check it fits on the board
            test.append(board[icoord][jcoord].buffer_or_taken)
        else:
            return False #because no room on board for ship

    if True in test: #one of the squares we looked at is taken
        return False #ship does not fit
    else:
        return True #ship fits


def mark_ship_on_board(board, starti, startj, direction, ship_size):
    starti = int(starti)
    startj = int(startj)
    if direction == 1: #1 across, 0 down
        i, j = 0, 1
    else:
        j, i = 0, 1

    for count in range(ship_size):
        icoord = int(starti+(count*i))
        jcoord = int(startj+(count*j))
        #print 'coords: ', icoord, jcoord
        board[icoord][jcoord].ship = True
        board[icoord][jcoord].buffer_or_taken = True
        #Now mark buffer around square of the the ship:
        if icoord != 0:
            board[icoord-1][jcoord].buffer_or_taken = True
        if icoord < (len(board) -1):
            board[icoord+1][jcoord].buffer_or_taken = True
        if  jcoord != 0:
            board[icoord][jcoord-1].buffer_or_taken = True
        if jcoord < (len(board) -1):
            board[icoord][jcoord+1].buffer_or_taken = True
    #mark corners as buffers:
    if direction == 1:
        right = ship_size
        down = 1
    if direction == 0:
        right = 1
        down = ship_size

    if starti != 0 and startj != 0:
        board[starti-1][startj-1].buffer_or_taken = True #topleft
    if starti != 0 and (startj+right) < (len(board)-1):
        board[starti-1][startj+right].buffer_or_taken = True #topright
    if (starti+down) < (len(board)-1) and startj != 0:
        board[starti+down][startj-1].buffer_or_taken = True #bottomleft
    if (starti+down) < (len(board)-1) and (startj+right) < (len(board)-1):
        board[starti+down][startj+right].buffer_or_taken = True #bottomright


def set_ship(board, ship_size):
    directions = [0, 1] #0 = down, 1= right
    options = [] #store all possible options:

    for direction in directions:
        for i in range(len(board)): #iterate through rows
            for j in range(len(board)): #iterate through columns
                if does_ship_fit_here(board, i, j, direction, ship_size) == True:
                    options.append([board[i][j].id, direction])

    #choose randomly
    from random import randint
    if len(options)>1:
        random_option = randint(0,(len(options)-1))
    elif len(options) == 1:
        random_option = 0
    else:
        print 'no space on the board for this ship'
        return
    id_of_chosen_square = options[random_option][0]
    direction = options[random_option][1]

    import math
    #converting to and from ids to index could be a seperate function???
    starti = math.floor(id_of_chosen_square/len(board)) #get row
    startj = id_of_chosen_square - (starti*len(board))
    mark_ship_on_board(board, starti, startj, direction, ship_size)


def set_ships(board, *args):
    #print 'set_ships', args
    for ar in args:
        set_ship(board, ar)


def get_ready_to_use_board():
    board = set_board(10)
    set_ships(board, 5, 4, 3, 2, 1)
    return board
