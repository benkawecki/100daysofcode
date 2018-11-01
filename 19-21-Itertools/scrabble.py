'''
This Bite focusses on the use of itertools. To that extend you complete
get_possible_dict_words and _get_permutations_draw to get all valid dictionary
words for a random draw of 7 letters.

This is fed into the tests that calculate the word with maximum value
(work previously done for Bite 3) and there you go: you have a Scrabble cheat
tool (Scrabble fans, pay attention or maybe skip this Bite!).

For example a draw of letters G, A, R, Y, T, E, V would give highest valued
word GARVEY (13 points).
'''


from itertools import permutations
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    my_dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    words = _get_permutations_draw(draw)
    legal = [word for word in words if word in my_dictionary]
    return legal


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    all_letter_combinations = set()
    for i in range(len(draw)):
        for tup in permutations(draw, i):
            all_letter_combinations.add(''.join(tup))

    return all_letter_combinations


if __name__ == '__main__':
    letters = 'garytev'
    print(get_possible_dict_words(letters))
