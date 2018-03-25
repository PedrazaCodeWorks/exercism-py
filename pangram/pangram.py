import string

def is_pangram(sentence):

    alpha = string.ascii_lowercase
    chars_found = []

    for c in sentence.lower():
        if c in alpha:
            chars_found.append(c)

    for c in alpha: 
        if c not in chars_found:
            return False

    return True

