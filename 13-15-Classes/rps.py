'''
Ben Kawecki

Rock Paper Scissors
'''
from actors import Roll, Player
from random import choice


def print_header():
    print('==============================')
    print('WELCOME TO ROCK PAPER SCISSORS')
    print('==============================')


def get_players_name():
    name = input('What is your name? ')
    p1 = Player(name)
    print('Welcome {}!'.format(p1.name))
    p2 = Player('Computer')
    return (p1, p2)


def build_the_three_rolls():
    rock = Roll('rock')
    paper = Roll('paper')
    scissors = Roll('scissors')
    return [rock, paper, scissors]


def game_loop(rolls, p1, p2):
    while True:
        if p1.wins >= 3:
            winner = p1.name
            break

        elif p2.wins >= 3:
            winner = p2.name
            break

        cmd = input('[R]ock, [P]aper, or [S]cissors: ').lower()

        if cmd == 'r':
            p1.roll = rolls[0]
        elif cmd == 'p':
            p1.roll = rolls[1]
        elif cmd == 's':
            p1.roll = rolls[2]
        else:
            print('Please enter a valid roll')
            continue

        p2.roll = choice(rolls)
        if p1.roll.batles(p2.roll):
            p1.wins += 1
            print('{} beats {}...point for {}!'.format(
                                                p1.roll.name,
                                                p2.roll.name,
                                                p1.name))

        elif p1.roll.batles(p2.roll) is False:
            p2.wins += 1
            print('{} beats {}...point for {}!'.format(
                                                p2.roll.name,
                                                p1.roll.name,
                                                p2.name))
        else:
            print('Tie!')

        print()
        print(f'{p1.name}-{p1.wins} vs {p2.name}-{p2.wins}')
        print()
    print('{} is the winner!'.format(winner))
    print('Thanks for playing!')


def main():
    print_header()
    rolls = build_the_three_rolls()
    player1, player2 = get_players_name()
    game_loop(rolls, player1, player2)


if __name__ == '__main__':
    main()
