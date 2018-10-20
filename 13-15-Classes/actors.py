'''
Ben Kawecki

Contains the classes necessary for rps.py

Contains: Roll, Player
'''


class Roll:
    ''' Represents a roll in rock paper scissors'''

    def __init__(self, name):
        self._allowed = {'rock', 'paper', 'scissors'}
        if name.lower() not in self._allowed:
            raise ValueError('roll must be in rock, paper, scissors')
        self.name = name.lower()

    def __repr__(self):
        return '{}({})'.format(self.__class__, self.name)

    def battles(self, other):
        '''takes two rock objects and returns the winning rock or None'''
        rules = {'rock': 'scissors',
                 'paper': 'rock',
                 'scissors': 'paper'}

        if rules[self.name] == other.name:
            return self
        elif rules[other.name] == self.name:
            return other
        else:
            return None


class Player:
    ''' Represents a player in our game'''
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def __repr__(self):
        return '{}()'.format(self.__class__, self.name)
