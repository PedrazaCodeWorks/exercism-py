def is_isogram(s):
    s = s.lower()
    visited = []
    ignore = [' ', '-']

    for c in s:
        if c not in ignore:
            if c not in visited:
                visited.append(c)
            else: 
                return False
    return True
