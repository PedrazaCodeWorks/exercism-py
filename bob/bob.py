import string

def hey(phrase):
    p = phrase.strip()

    if p == '':
        return "Fine. Be that way!"

    elif p[-1] == '?':
        if is_all_caps(p[:-1]):
            return "Calm down, I know what I'm doing!"

        return "Sure."

    elif is_all_caps(p):
        return "Whoa, chill out!"

    return "Whatever."

def is_all_caps(s):

    punct = [p for p in string.punctuation]
    res = [c for c in s.replace(' ', '') if c not in punct and not str.isdigit(c)]

    if res == []:
        return False

    for c in res:
        if(c.islower()):
            return False

    return True
