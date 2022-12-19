def break_words(stuff):
    """this function will break up words for us"""
    words = stuff.split('')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off. """
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    word = words.pop(-1)
    print(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_words(words)

def print_first_and_last_sorted(sentence):
    """Sorts the word then prints the first and last one."""
    words = sort_sentance(sentence)
    print_the_word(words)
    print_last_word(words)

    