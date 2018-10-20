'''
Ben Kawecki

Rock Paper Scissors
'''
from actors import Roll, Player


def print_header():
    print('==============================')
    print('WELCOME TO ROCK PAPER SCISSORS')
    print('==============================')


def get_players_name():
    p1 = 'Ben'
    p2 = 'Computer'
    return (p1, p2)


def build_the_three_rolls():
    rock = Roll('rock')
    paper = Roll('paper')
    scissors = Roll('scissors')
    return [rock, paper, scissors]


def game_loop(rolls, p1, p2):
    pass


def main():
    print_header()
    rolls = build_the_three_rolls()
    print(rolls[0].battles(rolls[1]))
    # player1, player2 = get_players_name()
    # game_loop(rolls, player1, player2)



if __name__ == '__main__':
    main()
