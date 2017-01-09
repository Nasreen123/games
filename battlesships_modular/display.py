def display_board(board):


    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


    print '    ',
    for number in range(1,11,1):
        print ' | ', number,
    print  '|\n  -----------------------------------------------------------------'

    for i in range(len(board)):
        print '  ', alphabet[i],
        for square in board[i]:
            if square.shown == False:
                print ' |   ',
            elif square.shown == True and square.ship == True:
                print ' |  S',
            else:
                print ' |  x',
        print ' |\n  -----------------------------------------------------------------'
