def get_input():
    print 'Choose a square!'
    user_input = raw_input('-->').upper()
    print 'You guessed ', user_input
    return user_input


def split_input(user_input):
    if len(user_input) == 3:
        if is_a_number(user_input[0:2]):
            #print 'user_input[0:2] is a number', user_input[0:2]
            num = user_input[0:2]
            let = user_input[2]
        elif is_a_number(user_input[1:]):
            #print 'user_input[1:] is a number', user_input[1:]
            num = user_input[1:]
            let = user_input[0]
        else:
            return ([False])
    elif len(user_input) == 2:
        if is_a_number(user_input[0]):
            num = user_input[0]
            let = user_input[1]
        elif is_a_number(user_input[1]):
            num = user_input[1]
            let = user_input[0]
        else:
            return ([False])
    else:
        return ([False])
    return (True, num, let)


def convert_input(num, let):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = [str(number) for number in range(1,11)]
    if let in alphabet and num in numbers:
        i = alphabet.index(let)
        j = numbers.index(num)
        return (True, i, j)
    else:
        print 'invalid input, try again'
        return ([False])


def is_a_number(something):
    try:
        float(something)
        return True
    except ValueError:
        return False

def process_input(user_input):
    input_tuple = split_input(user_input)
    if input_tuple[0] == True:
        return convert_input(input_tuple[1],input_tuple[2])
    else:
        return ([False])
