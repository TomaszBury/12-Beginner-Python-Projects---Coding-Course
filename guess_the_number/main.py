from ast import While
import random
upper_bound = random.randint(1, 100)

print(f'Lets play the game:\nGuess the number bettween: 1 and {upper_bound}!')


def guess(bound):
    random_number = random.randint(1, bound)

    guess = user_number('pick the number: ')
    '''
    print(f'{type(random_number)} and guess type: {type(guess)}')

    if random_number == guess:
        print('\nAbracadabra!\n')
    '''

    while(guess != random_number):
        '''
        print(f'Random number is: {random_number}')
        print(f'guess is: {guess}')
        '''
        if guess > random_number:
            guess = user_number('Wrong number try lower: ')
        elif guess < random_number:
            guess = user_number('Wrong number try higher: ')

    print(f'You have guessed the number! {random_number}')


def computer_guess(bound):
    looking_for = user_number('What number you want computer to look for: ')
    low = 1
    high = bound
    computer_guess = random.randint(low, high)

    while looking_for != computer_guess:
        print(f'your hoice: {looking_for}, PC: {computer_guess}')
        if computer_guess > looking_for:
            high = computer_guess
            computer_guess = random.randint(low, high)
        elif computer_guess < looking_for:
            low = computer_guess
            computer_guess = random.randint(low, high)

    print(f'Computer have guessed the number! {computer_guess}')


def user_number(question):
    return int(input(question))


def menu():
    quit = True
    while quit:
        you_vs_pc = input(
            'Do you (Y) want to decide or PC (P).\n(Q) to quit').upper()
        if you_vs_pc == 'Y':
            guess(upper_bound)
        elif you_vs_pc == 'P':
            computer_guess(upper_bound)
        elif you_vs_pc == 'Q':
            quit = False
        else:
            print(
                "Your choices lead you here.\n\nTerminated\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            quit = False


menu()
