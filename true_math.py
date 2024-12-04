from math import inf


def true_divide(first, second):
    if second == 0:
        return inf
    if first > 0:
        result = first / second
        return result
    else:
        return "You enter wrong number"




