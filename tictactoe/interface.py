#Displays the board on the terminal
def display_board(board):
    line = ' ---------------------------------\n'
    print '\n      |   A    |    B   |    C   |\n'

    for x in range(3):
        print line
        print ' ', x + 1 ,' ',
        for y in range(3):
            square_index = 3 * x + y
            if board.squares[square_index].empty:
                print '|       ',
            else:
                print '|   ', board.squares[square_index].player, ' ',
        print '|\n'

#Gets input from the user
def get_input():
    user_input = raw_input('----->>>>').upper()
    return user_input

#Checks the input is valid, and converts to square index
def process_input(user_input):
    rows = {'1':0, '2':3, '3':6} #row input codes and values
    columns = {'A':0, 'B':1, 'C':2} #column input codes and values
    #Check the input has one column (A/B/C) and one row (1/2/3)
    #Get the value of the inputs and store in square
    if len(user_input) == 2 and user_input[0] in columns and user_input[1] in rows:
        square = columns[(user_input[0])] + rows[(user_input[1])]
    elif len(user_input) ==2 and user_input[0] in rows and user_input[1] in columns:
        square = rows[(user_input[0])] + columns[(user_input[1])]
    else:
        return (False, 0)
    return (True, square)
