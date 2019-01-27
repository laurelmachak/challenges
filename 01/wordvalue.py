from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    word_list = []
    with open(DICTIONARY, 'r') as f:
        for line in f:
            word_list.append(line.strip())
            
    return word_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word_value = 0
    for letter in word:
        try:
            word_value += LETTER_SCORES[letter.upper()]
        except KeyError:
            pass

    return word_value

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    all_word_values = {}
    for word in words:
        all_word_values[word] = calc_word_value(word)

    highest_value = 0
    highest_word = None

    for key, value in all_word_values.items():
        if value > highest_value:
            highest_value = value
            highest_word = key

    return highest_word

    
    

if __name__ == "__main__":
    pass # run unittests to validate
