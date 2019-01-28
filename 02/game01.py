#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""
    # Create a copy of POUCH list so we don't modify a global variable
    draw_pile = []
    for tile in POUCH:
        draw_pile.append(tile)

    letters_drawn = []
    for i in range(NUM_LETTERS):
        highest_index = len(draw_pile) - 1
        random_index = random.randint(0,highest_index)
        letters_drawn.append(draw_pile.pop(random_index))
    
    return letters_drawn


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    user_word = None

    # keep asking for user input until _validation returns True
    while (user_word is None) or (_validation(user_word, draw) is False):
        user_word = input("Form a valid word: ")
    
    return user_word



def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""

    # Create copy of draw list as to not modify draw
    available_letters = []
    for letter in draw:
        available_letters.append(letter)
    
    # make all letters uppercase to match case of deal
    word = word.upper()

    for letter in word:
        if letter != '-':
            if letter not in available_letters:
                return False
            else:
                available_letters.remove(letter)

    # make all letters lower case to match case of dictionary words
    # TODO make the other data structures all have lower case from beginning to not have to do this so much
    word = word.lower()
    if word in DICTIONARY:
        return True
    else:
        return False


# From challenge 01:
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# Below 2 functions pass through the same 'draw' argument (smell?).
# Maybe you want to abstract this into a class?
# get_possible_dict_words and _get_permutations_draw would be instance methods.
# 'draw' would be set in the class constructor (__init__).
def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    possible_dict_words = []
    draw_perms = _get_permutations_draw(draw)
    for item in draw_perms:
        if item in DICTIONARY:
            possible_dict_words.append(item)
    
    return possible_dict_words


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    draw_permutations = []
    for i in range(len(draw)):
        result = itertools.permutations(draw, i+1)
        for item in result:
            item_string = ''.join(item).lower()
            # make sure no repeated words, for example if double letters in draw
            if item_string not in draw_permutations:
                draw_permutations.append(item_string)
    
    return draw_permutations


# From challenge 01:
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def main():
    """Main game interface calling the previously defined methods"""
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = word_score / max_word_score * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
