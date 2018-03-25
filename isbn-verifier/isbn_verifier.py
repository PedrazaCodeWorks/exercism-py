def verify(isbn):
    isbn_digits = []

    for i, c in enumerate(isbn.replace('-', '')):
        if c.isdigit():
            isbn_digits.append(int(c))

        elif c == 'X':
            if i == 9:
                isbn_digits.append(10)
            else:
                return False

    return is_isbn(isbn_digits)


def is_isbn(digits):
    if len(digits) != 10:
        return False

    coeff = 10
    res = 0

    for digit in digits:
        res += (coeff * digit)
        coeff -= 1

    if res % 11 == 0:
        return True

    return False




