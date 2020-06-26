from random import randint


rps_dict = {
    '1': 'ROCK',
    '2': 'PAPER',
    '3': 'SCISSOR'
}


def compair(a, b):
    if a == b: return 'DRAW'
    if a == 'ROCK':
        if b == 'PAPER':
            return b
        else:  # 'SCISSOR'
            return a
    elif a == 'PAPER':
        if b == 'ROCK':
            return a
        else:  # 'SCISSOR'
            return b
    else:
        if b == 'ROCK':
            return b
        else:  # 'PAPER'
            return a


def get_player_choice():
    choice = input('1-ROCK 2-PAPER 3-SCISSOR: ')
    if choice in '123':
        return rps_dict[choice]
    else:
        print('Not available; Choose between 1, 2 and 3.')
        return get_player_choice()


def get_computer_choice():
    choice = str(randint(1, 3))
    return rps_dict[choice]


def display_choices(player, computer):
    print('Player\'s choice: {c}'.format(c=player))
    print('Computer\'s choice: {c}'.format(c=computer))


def play_again():
    choice = input('Play again? (y: yes)')
    if choice != 'y':
        quit()


def main():
    while True:
        player = get_player_choice()
        computer = get_computer_choice()
        print()

        display_choices(player, computer)
        res = compair(player, computer)
        print()

        print('{winner} wins.'.format(winner=res) if res != 'DRAW' else 'DRAW')

        play_again()
        print()

if __name__ == '__main__':
    main()
